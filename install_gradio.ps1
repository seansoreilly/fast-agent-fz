#!/usr/bin/env pwsh
# install_gradio.ps1 - Script to install Gradio and dependencies for Fat Zebra Agent UI

# Ensure the virtual environment exists
if (-not (Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# Activate the virtual environment
Write-Host "Activating virtual environment..."
.\.venv\Scripts\Activate.ps1

# Install requirements including Gradio
Write-Host "Installing requirements including Gradio..."
pip install -r requirements.txt

Write-Host "Gradio installation completed successfully!" 