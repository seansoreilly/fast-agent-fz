#!/bin/bash
# install_gradio.sh - Script to install Gradio and dependencies for Fat Zebra Agent UI

# Check Python version
python_version=$(python3 --version 2>&1)
if [[ ! $python_version == *"3.12"* ]]; then
    echo "WARNING: This application requires Python 3.12.7 or higher"
    echo "Current Python version: $python_version"
    echo "Please install Python 3.12.7+ before continuing"
    exit 1
fi

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