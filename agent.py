"""Fat Zebra AI agent implementation using Fast Agent MCP framework."""

import asyncio
import os
import glob
import logging
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

        for md_file in markdown_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    logger.info("Loading documentation: %s", md_file)
                    await agent.with_resource(
                        content,     # message (description)
                        content      # content of the file
                    )
                    logger.debug("Successfully loaded: %s (%s bytes)", md_file, len(content))
            except (IOError, UnicodeDecodeError) as e:
                logger.error("Failed to load %s: %s", md_file, str(e))

        logger.info("All documentation resources loaded")
        await agent()


if __name__ == "__main__":
    asyncio.run(main())
