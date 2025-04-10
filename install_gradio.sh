#!/bin/bash
# install_gradio.sh - Script to install Gradio and dependencies for Fat Zebra Agent UI

# Ensure the virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install requirements including Gradio
echo "Installing requirements including Gradio..."
pip install -r requirements.txt

echo "Gradio installation completed successfully!"

# Make the script executable
chmod +x install_gradio.sh 