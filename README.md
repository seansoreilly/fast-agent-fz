# Fast Agent FZ

A Fat Zebra AI agent built using the Fast Agent MCP framework.

## Overview

This project implements an AI agent using the Fast Agent framework, specifically configured for Fat Zebra integration. The agent is designed to be helpful and can interact with multiple services including fetch, filesystem, and Fat Zebra servers.

## Project Structure

```
.
├── agent.py              # Main agent implementation file
├── fastagent.config.yaml # Agent configuration
├── requirements.txt      # Python dependencies
├── templates/           # Template directory
├── logs/               # Log files directory
├── gradio_app.py       # Gradio UI implementation (coming soon)
└── .venv/              # Python virtual environment
```

## Prerequisites

- Python 3.x
- Node.js (for some dependencies)
- Git

## Dependencies

### Python Dependencies

The project relies on several Python packages:

- anthropic >= 0.5.0
- fastapi >= 0.100.0
- uvicorn >= 0.22.0
- pydantic >= 2.0.0
- python-dotenv >= 1.0.0
- requests >= 2.31.0
- pyyaml >= 6.0
- jinja2 >= 3.1.2
- aiohttp >= 3.8.5
- websockets >= 11.0.3
- gradio >= 4.13.0
- fast-agent-mcp (from GitHub)

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Node.js dependencies:
   ```bash
   npm install
   ```
5. Install Gradio UI dependencies:

   ```bash
   # On Windows
   .\install_gradio.ps1

   # On Unix-based systems
   ./install_gradio.sh
   ```

## Configuration

The project uses two configuration files:

- `fastagent.config.yaml`: Main configuration file
- `fastagent.secrets.yaml`: Secrets and sensitive configuration (not tracked in git)

## Usage

### Terminal-based Agent

To run the agent in the terminal:

```bash
python agent.py
```

You can modify the model using the `--model` command line switch or through agent arguments.

### Gradio UI (Coming Soon)

To run the agent with the Gradio web interface:

```bash
python gradio_app.py
```

This will start a web server at http://localhost:7860 where you can interact with the agent through a user-friendly chat interface.

## Development

The main agent logic is in `agent.py`. The agent is configured to work with:

- Fetch server
- Filesystem server
- Fat Zebra server

Gradio UI implementation is in progress and will provide a more user-friendly interface for interacting with the agent.

## Security

- Sensitive information should be stored in `fastagent.secrets.yaml`
- The `.gitignore` file is configured to exclude sensitive files and directories
