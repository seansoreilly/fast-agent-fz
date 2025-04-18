"""Gradio web interface for the Fat Zebra AI Assistant."""

import os
import logging
import gradio as gr
from agent import fast, generate_response

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("gradio-app")

# Ensure the static directory exists
os.makedirs("static", exist_ok=True)

# Agent state manager
class AgentState:
    """Maintains the state of the Fat Zebra agent across chat requests."""
    def __init__(self):
        self.agent = None

agent_state = AgentState()

async def chat_interface(message,history):
    """Process messages through the Fat Zebra agent."""
    # Initialize the agent if needed
    if agent_state.agent is None:
        logger.info("Initializing persistent agent")
        # Create the context using async with
        async with fast.run() as agent:
            agent_state.agent = agent

    # Use the existing generate_response function
    response = await generate_response(agent_state.agent, message)
    return response

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_interface,
    title="Fat Zebra AI Assistant",
    description="Ask me anything about Fat Zebra payments, transactions, or API usage.",
    type="messages",
    theme="soft",
    examples=[
        "Do a test payment and explain it?",
        "What's the process for issuing a refund?",
        "How do I tokenize a card?",
        "What are the parameters for a direct debit payment?"
    ]
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        pwa=True,
        show_error=True,
        share=True,
        favicon_path="static/5f03e4e6c8c68511212f0c40_FZ_Favicon_32x32.png",
        app_kwargs={
            "head_html": """
                <link rel="manifest" href="/static/manifest.json">
                <meta name="theme-color" content="#ffffff">
                <link rel="apple-touch-icon" href="/static/5f03e4e6c8c68511212f0c40_FZ_Favicon_32x32.png">
            """
        })
