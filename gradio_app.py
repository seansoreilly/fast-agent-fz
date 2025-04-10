import gradio as gr
import asyncio
from agent import fast, generate_response

async def process_message(message, history):
    """Process a user message through the Fat Zebra agent."""
    async with fast.run() as agent:
        # Pass the message to the agent and get the response
        response = await generate_response(agent, message)
        return response

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=process_message,
    title="Fat Zebra AI Assistant",
    description="Ask me anything about Fat Zebra payments, transactions, or API usage.",
    theme="soft",
    examples=[
        "How do I process a credit card payment?",
        "What's the process for issuing a refund?",
        "How do I tokenize a card?",
        "What are the parameters for a direct debit payment?"
    ]
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860) 