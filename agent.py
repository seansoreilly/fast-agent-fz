"""Fat Zebra AI agent implementation using Fast Agent MCP framework."""

import asyncio
from mcp_agent import FastAgent

# Create the application
fast = FastAgent("Fat Zebra AI")


# Define the agent
@fast.agent(instruction="Assist with any queries regarding the Fat Zebra API", servers=["fetch","filesystem","fatzebra"])
async def main():
    """Run the Fat Zebra AI agent in an async context."""
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent()


if __name__ == "__main__":
    asyncio.run(main())
