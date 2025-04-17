#!/usr/bin/env pwsh
# install_gradio.ps1 - Script to install Gradio and dependencies for Fat Zebra Agent UI

# Check Python version
$pythonVersion = python --version
if (-not $pythonVersion.Contains("3.12")) {
    Write-Host "WARNING: This application requires Python 3.12.7 or higher" -ForegroundColor Red
    Write-Host "Current Python version: $pythonVersion" -ForegroundColor Red
    Write-Host "Please install Python 3.12.7+ before continuing" -ForegroundColor Red
    exit 1
}

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