# Gradio Implementation Plan for Fat Zebra Agent UI

## Overview

This plan outlines the steps to implement a Gradio-based chat interface for the existing Fat Zebra AI agent. The new UI will replace the current terminal.html interface with a more user-friendly, feature-rich chat experience while maintaining the core functionality of the Fast Agent MCP framework.

## Project Goals

- Create an intuitive chat interface for interacting with the Fat Zebra AI agent
- Maintain all existing functionality of the agent
- Enable streaming responses for better user experience
- Add helpful UI elements specific to payment processing
- Keep the implementation lightweight and maintainable

## Implementation Steps

### Phase 1: Environment Setup ✅

- ✅ Install Gradio and required dependencies:
  ```bash
  pip install gradio
  ```
- ✅ Add Gradio to `requirements.txt`:
  ```
  gradio>=4.13.0
  ```
- ✅ Create setup scripts for easier installation:
  - `install_gradio.ps1` for Windows
  - `install_gradio.sh` for Unix-based systems

### Phase 2: Basic Chat Interface Implementation

- Create a new file `gradio_app.py` in the project root with the following structure:

  ```python
  import gradio as gr
  import asyncio
  from mcp_agent import FastAgent

  # Create the Fat Zebra agent
  fast = FastAgent("Fat Zebra AI")

  async def process_message(message, history):
      """Process a user message through the Fat Zebra agent."""
      async with fast.run(instruction="Assist with any queries regarding the Fat Zebra API",
                          servers=["fetch", "filesystem", "fatzebra"]) as agent:
          # Pass the message to the agent and get the response
          response = await agent.generate_response(message)
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
      ],
      retry_btn=True,
      undo_btn=True,
      clear_btn="Clear Chat"
  )

  if __name__ == "__main__":
      demo.launch(server_name="0.0.0.0", server_port=7860)
  ```

### Phase 3: Adapt Fat Zebra Agent for Gradio

- Modify `agent.py` to include a function for generating responses within an existing agent session:

  ```python
  """Fat Zebra AI agent implementation using Fast Agent MCP framework."""

  import asyncio
  from mcp_agent import FastAgent

  # Create the application
  fast = FastAgent("Fat Zebra AI")

  # Function to generate responses (for Gradio integration)
  async def generate_response(agent, message):
      """Generate a response to a user message."""
      # Process the message and return the response
      response = await agent.process_message(message)
      return response

  # Define the agent
  @fast.agent(instruction="Assist with any queries regarding the Fat Zebra API", servers=["fetch","filesystem","fatzebra"])
  async def main():
      """Run the Fat Zebra AI agent in an async context."""
      # use the --model command line switch or agent arguments to change model
      async with fast.run() as agent:
          # Add the generate_response method to the agent
          agent.generate_response = lambda message: generate_response(agent, message)
          await agent()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

### Phase 4: Enhanced UI Features

- Add payment-specific UI components in `gradio_app.py`:

  ```python
  with gr.Blocks(theme=gr.themes.Soft()) as demo:
      gr.Markdown("# Fat Zebra AI Assistant")

      with gr.Tab("Chat"):
          chatbot = gr.ChatInterface(
              fn=process_message,
              title="Fat Zebra AI Assistant",
              description="Ask me anything about Fat Zebra payments, transactions, or API usage.",
              examples=[
                  "How do I process a credit card payment?",
                  "What's the process for issuing a refund?",
                  "How do I tokenize a card?",
                  "What are the parameters for a direct debit payment?"
              ],
              retry_btn=True,
              undo_btn=True,
              clear_btn="Clear Chat"
          )

      with gr.Tab("Payment Form Templates"):
          gr.Markdown("## Common Payment Forms")
          with gr.Accordion("Credit Card Payment"):
              gr.Code(
                  label="Credit Card Payment Example",
                  language="json",
                  value="""
                  {
                      "amount": 1000, // in cents, e.g., $10.00
                      "card_number": "4111111111111111",
                      "card_holder": "Test User",
                      "card_expiry": "12/2025",
                      "card_cvv": "123",
                      "reference": "INV-123",
                      "currency": "AUD",
                      "customer_ip": "127.0.0.1"
                  }
                  """
              )

          with gr.Accordion("Direct Debit Payment"):
              gr.Code(
                  label="Direct Debit Payment Example",
                  language="json",
                  value="""
                  {
                      "amount": 1000,
                      "account_name": "Test Account",
                      "account_number": "12345678",
                      "bsb": "123-456",
                      "reference": "INV-123",
                      "description": "Monthly payment"
                  }
                  """
              )

      with gr.Tab("API Documentation"):
          gr.Markdown("""# Fat Zebra API Quick Reference

          ## Key Endpoints

          - **Credit Card Payment**: `/fat_zebra_payment`
          - **3D Secure Payment**: `/fat_zebra_3d_secure`
          - **Tokenize Card**: `/fat_zebra_tokenize`
          - **Token Payment**: `/fat_zebra_token_payment`
          - **Direct Debit**: `/fat_zebra_direct_debit`
          - **Refund**: `/fat_zebra_refund`

          For full documentation, ask the assistant or refer to the official Fat Zebra documentation.
          """)

  if __name__ == "__main__":
      demo.launch(server_name="0.0.0.0", server_port=7860)
  ```

### Phase 5: Response Streaming Implementation

- Implement streaming responses for a better user experience:

  ```python
  async def process_message_stream(message, history):
      """Process a user message through the Fat Zebra agent with streaming response."""
      async with fast.run(instruction="Assist with any queries regarding the Fat Zebra API",
                          servers=["fetch", "filesystem", "fatzebra"]) as agent:
          # Set up streaming response
          response_parts = []
          async for response_part in agent.generate_response_stream(message):
              response_parts.append(response_part)
              yield "".join(response_parts)

  # Use streaming in the chat interface
  chatbot = gr.ChatInterface(
      fn=process_message_stream,
      # ... other parameters remain the same
  )
  ```

### Phase 6: Integration Testing

- Test the Gradio UI with various Fat Zebra API queries:
  - Card processing scenarios
  - Tokenization workflows
  - Refund processes
  - Error handling cases
- Verify that all MCP servers are correctly accessed through the new interface

### Phase 7: Deployment Updates

- Update the project README.md with new launching instructions
- Create a simple startup script for the Gradio interface:

  ```bash
  #!/bin/bash
  # start_ui.sh

  source .venv/bin/activate
  python gradio_app.py
  ```

## Technical Considerations

1. **Async Compatibility**: Ensure Gradio works correctly with the async nature of the Fast Agent MCP framework.

2. **Error Handling**: Implement robust error handling for both agent and UI failures.

3. **Environment Variables**: Maintain compatibility with existing environment configuration.

4. **Resource Usage**: Monitor memory and CPU usage as Gradio adds an additional layer to the stack.

5. **Security**: Maintain existing security measures while adding the new UI layer.

## Timeline

1. **Phase 1 - Environment Setup**: 1 day
2. **Phase 2 & 3 - Core Chat Functionality**: 2 days
3. **Phase 4 - Enhanced UI Features**: 2 days
4. **Phase 5 - Streaming & Response Formatting**: 1 day
5. **Phase 6 - Testing & Bug Fixes**: 2 days
6. **Phase 7 - Documentation & Deployment**: 1 day

**Total Estimated Time**: 9 days

## Future Enhancements

- Add user authentication for the Gradio interface
- Implement chat history persistence
- Add visualization components for transaction data
- Create a dashboard for monitoring transaction statistics
- Support for dark/light theme toggle
