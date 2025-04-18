"""Gradio web interface for the Fat Zebra AI Assistant."""

import os
import logging
import gradio as gr
from gradio.themes.base import Base
from agent import fast, generate_response

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("gradio-app")

os.makedirs("static", exist_ok=True)

# Check if header image exists
HEADER_PATH = "static/fz_skin/header.png"
print(f"Header image path: {os.path.abspath(HEADER_PATH)}")
print(f"Header image exists: {os.path.exists(HEADER_PATH)}")

# Fat Zebra theme based on branding
fz_theme = gr.themes.Default(
    primary_hue="blue",
    secondary_hue="gray",
    font=["Open Sans", "Montserrat", "Fira Sans", "Roboto", "sans-serif"]
)

# Agent state manager
class AgentState:
    """Maintains the state of the Fat Zebra agent across chat requests."""
    def __init__(self):
        self.agent = None

agent_state = AgentState()

async def chat_interface(message, history):
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

# Create the Gradio interface with header image
with gr.Blocks(theme=fz_theme, css=open("static/fz_skin/custom.css", encoding="utf-8").read()) as demo:
    with gr.Row(elem_classes="header-container"):
        gr.Image(
            value="static/fz_skin/header.png",
            show_label=False,
            container=False,
            elem_id="header-image"
        )

    chatbot = gr.ChatInterface(
        fn=chat_interface,
        title="",
        description="Ask me anything about Fat Zebra payments, transactions, or API usage.",
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
        server_port=7861,
        pwa=True,
        show_error=True,
        share=True,
        show_api=False,
        favicon_path="static/5f03e4e6c8c68511212f0c40_FZ_Favicon_32x32.png",
        app_kwargs={
            "head_html": """
                <link rel="manifest" href="/static/manifest.json">
                <meta name="theme-color" content="#ffffff">
                <link rel="apple-touch-icon" href="/static/5f03e4e6c8c68511212f0c40_FZ_Favicon_32x32.png">
            """
        }
    )
