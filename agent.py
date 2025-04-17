"""Fat Zebra AI agent implementation using Fast Agent MCP framework."""

import asyncio
import os
import glob
import logging
import tempfile
from pathlib import Path
from mcp_agent import FastAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("fatzebra-agent")

# Create the application
fast = FastAgent("Fat Zebra AI")

# Function to generate responses (for Gradio integration)
async def generate_response(agent, message):
    """Generate a response to a user message."""
    # Process the message and return the response
    response = await agent.send(message)
    return response

# Define the agent
@fast.agent(
    instruction="Assist with any queries regarding the Fat Zebra API",
    # servers=["fatzebra","brave_search_api"],
    servers=["fatzebra"],
    use_history=True
)
async def main():
    """Run the Fat Zebra AI agent in an async context."""
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        # Create a sync wrapper for the async generate_response function
        def sync_generate_response(message):
            """Synchronous wrapper for the async generate_response function."""
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            # Run the async function and return its result
            result = loop.run_until_complete(generate_response(agent, message))
            loop.close()
            return result

        # Add the generate_response method to the agent
        agent.generate_response = sync_generate_response

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
                    
                    # Try direct content loading first
                    try:
                        await agent.send(
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
                        await agent.send(user_msg)
                        
                        if len(category_content) > 10000:
                            logger.warning("Content for %s was truncated (too large)", category)
                        
                        logger.info("Successfully loaded %s documentation with %s files using fallback",
                                   category, len(documents))
                except Exception as e:
                    logger.error("Failed to load %s documentation: %s", category, str(e))
            
            logger.info("All documentation resources loaded")
            await agent()
            
        finally:
            # Clean up temporary files when done
            import shutil
            try:
                shutil.rmtree(temp_dir)
                logger.info("Cleaned up temporary directory: %s", temp_dir)
            except Exception as e:
                logger.error("Failed to clean up temporary directory: %s", str(e))


if __name__ == "__main__":
    asyncio.run(main())
