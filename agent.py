"""Fat Zebra AI agent implementation using Fast Agent MCP framework."""

import asyncio
import os
import glob
import logging
import tempfile
import argparse
import random
import time
from pathlib import Path
from mcp_agent import FastAgent
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("fatzebra-agent")

# Create the application
fast = FastAgent("Fat Zebra AI")

# Retry decorator with exponential backoff for API calls
def retry_with_exponential_backoff(
    max_retries=5, 
    initial_delay=0.2,  # Much shorter initial delay
    exponential_base=2,
    jitter=True,
    retry_codes={429, 500, 502, 503, 504, 529}
):
    """
    Decorator for implementing retry logic with exponential backoff.
    
    Args:
        max_retries: Maximum number of retries
        initial_delay: Initial delay between retries in seconds (starting with 0.2s)
        exponential_base: Base of the exponential backoff
        jitter: Whether to add random jitter to the delay
        retry_codes: HTTP status codes that should trigger a retry
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Initialize variables
            num_retries = 0
            delay = initial_delay
            
            while True:
                try:
                    # Try executing the function
                    return await func(*args, **kwargs)
                    
                except Exception as e:
                    # Extract status code if available
                    status_code = None
                    error_code = None
                    
                    # Try to get status code from exception properties
                    if hasattr(e, "status_code"):
                        status_code = e.status_code
                    elif hasattr(e, "response") and hasattr(e.response, "status_code"):
                        status_code = e.response.status_code
                    
                    # Try to parse error response for code
                    if hasattr(e, "response") and hasattr(e.response, "json"):
                        try:
                            error_response = e.response.json()
                            if isinstance(error_response, dict) and "code" in error_response:
                                error_code = error_response["code"]
                                # If status code wasn't available but code is, use code
                                if status_code is None and isinstance(error_code, int):
                                    status_code = error_code
                        except:
                            pass
                    
                    # Determine if we should retry
                    should_retry = (
                        (status_code in retry_codes or error_code in retry_codes) and 
                        num_retries < max_retries
                    )
                    
                    if not should_retry:
                        # Don't retry, just raise the exception
                        raise
                    
                    # Calculate delay with jitter if enabled
                    if jitter:
                        actual_delay = delay * (0.5 + random.random())
                    else:
                        actual_delay = delay
                    
                    # Log retry attempt
                    logger.warning(
                        f"Request failed with status {status_code}"
                        f"{f', code {error_code}' if error_code else ''}"
                        f". Retrying in {actual_delay:.2f} seconds... "
                        f"(Attempt {num_retries + 1}/{max_retries})"
                    )
                    
                    # Sleep before retry
                    await asyncio.sleep(actual_delay)
                    
                    # Increase delay and retry counter
                    delay *= exponential_base
                    num_retries += 1
        
        return wrapper
    
    return decorator

# Wrapped version of agent.send with retry logic
async def send_with_retry(agent, message):
    """Wrapped version of agent.send with retry logic."""
    @retry_with_exponential_backoff()
    async def _send_with_retry():
        return await agent.send(message)
    
    return await _send_with_retry()

# Function to generate responses (for Gradio integration)
async def generate_response(agent, message):
    """Generate a response to a user message."""
    # Process the message with retry logic and return the response
    response = await send_with_retry(agent, message)
    return response

async def load_documentation(agent):
    """Load documentation from markdown files."""
    # Load all markdown files from documentation directory
    doc_path = r"documentation"
    logger.info("Looking for documentation files in: %s", os.path.abspath(doc_path))
    markdown_files = glob.glob(os.path.join(doc_path, "**/*.md"), recursive=True)
    logger.info("Found %s documentation files", len(markdown_files))

    # Group documents by category based on their first directory
    document_groups = {}
    
    for md_file in markdown_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                file_name = os.path.basename(md_file)
                content = f.read()
                
                # Use relative path to determine category
                rel_path = os.path.relpath(md_file, doc_path)
                category = os.path.dirname(rel_path).split(os.path.sep)[0] or "general"
                
                # Initialize category if it doesn't exist
                if category not in document_groups:
                    document_groups[category] = []
                
                document_groups[category].append({
                    "name": file_name,
                    "content": content,
                    "path": md_file
                })
                
                logger.debug("Added to group %s: %s (%s bytes)",
                            category, md_file, len(content))
        except (IOError, UnicodeDecodeError) as e:
            logger.error("Failed to load %s: %s", md_file, str(e))
    
    # Create temp directory to store batched content files
    temp_dir = Path(tempfile.mkdtemp(prefix="fatzebra_docs_"))
    logger.info("Created temporary directory for docs: %s", temp_dir)
    
    try:
        # Load each document group as a batch
        for category, documents in document_groups.items():
            try:
                # Skip empty categories
                if not documents:
                    continue
                    
                # Create a message with all documents in this category
                doc_messages = []
                for doc in documents:
                    doc_messages.append(f"# {doc['name']}\n\n{doc['content']}")
                
                # Create content for this category
                category_content = f"## Fat Zebra {category.capitalize()} Documentation\n\n"
                category_content += "Use this documentation before searching the web\n\n---\n\n"
                category_content += "\n\n---\n\n".join(doc_messages)
                
                # Try direct content loading first with retry logic
                try:
                    await send_with_retry(
                        agent,
                        f"Please remember this {category.capitalize()} documentation for reference:\n\n{category_content}"
                    )
                    logger.info("Successfully loaded %s documentation with %s files using message",
                               category, len(documents))
                except Exception as e:
                    logger.warning("Could not load via message, trying alternative: %s", str(e))
                    
                    # Save to a temporary file as fallback
                    file_path = temp_dir / f"{category}_docs.md"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(category_content)
                    
                    # Send as user message with the documentation content
                    user_msg = f"Documentation for Fat Zebra {category.capitalize()} category with {len(documents)} files:\n\n{category_content[:10000]}"
                    await send_with_retry(agent, user_msg)
                    
                    if len(category_content) > 10000:
                        logger.warning("Content for %s was truncated (too large)", category)
                    
                    logger.info("Successfully loaded %s documentation with %s files using fallback",
                               category, len(documents))
            except Exception as e:
                logger.error("Failed to load %s documentation: %s", category, str(e))
        
        logger.info("All documentation resources loaded")
    finally:
        # Clean up temporary files when done
        import shutil
        try:
            shutil.rmtree(temp_dir)
            logger.info("Cleaned up temporary directory: %s", temp_dir)
        except Exception as e:
            logger.error("Failed to clean up temporary directory: %s", str(e))

@fast.agent(
    instruction="Assist with any queries regarding the Fat Zebra API",
    # servers=["fatzebra","brave_search_api"],
    servers=["fatzebra"],
    use_history=True
)
async def main():
    """Run the Fat Zebra AI agent in an async context."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Fat Zebra AI Agent')
    parser.add_argument('--load-docs', action='store_true', help='Load documentation files')
    parser.add_argument('--retry-initial-delay', type=float, default=0.2, 
                       help='Initial delay for retry logic (default: 0.2 seconds)')
    parser.add_argument('--retry-max', type=int, default=5,
                       help='Maximum number of retries (default: 5)')
    args = parser.parse_args()

    # Create a custom retry function with parameters from command line
    def create_custom_retry_wrapper(agent):
        async def custom_send_with_retry(message):
            @retry_with_exponential_backoff(
                initial_delay=args.retry_initial_delay,
                max_retries=args.retry_max
            )
            async def _custom_send_with_retry():
                return await agent.send(message)
            
            return await _custom_send_with_retry()
        return custom_send_with_retry

    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        # Assign custom retry function using command line args
        custom_retry = create_custom_retry_wrapper(agent)
        
        # Create a sync wrapper for the async generate_response function
        def sync_generate_response(message):
            """Synchronous wrapper for the async generate_response function."""
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            # Run the async function with custom retry and return its result
            async def _gen_response():
                return await custom_retry(message)
            result = loop.run_until_complete(_gen_response())
            loop.close()
            return result

        # Add the generate_response method to the agent
        agent.generate_response = sync_generate_response

        # Only load documentation if the --load-docs flag is passed
        if args.load_docs:
            # Use custom retry wrapper for documentation loading
            global send_with_retry
            send_with_retry = create_custom_retry_wrapper(agent)
            await load_documentation(agent)
        else:
            logger.info("Skipping documentation loading (use --load-docs to load)")

        await agent()

if __name__ == "__main__":
    asyncio.run(main())