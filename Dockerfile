FROM python:3.10-slim

WORKDIR /app

# Install system dependencies and node.js
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    git \
    gcc \
    python3-dev \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .

# Install pip-tools and upgrade pip
RUN pip install --no-cache-dir -U pip pip-tools

# Install dependencies
RUN pip install --no-cache-dir -v -r requirements.txt

# Install FastAgent directly
RUN pip install --no-cache-dir -v git+https://github.com/evalstate/fast-agent.git

# List installed packages for debugging
RUN pip list

# Remove any cached Python files
RUN find /app -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
RUN find /app -type f -name "*.pyc" -delete

# Copy FastAgent files
COPY agent.py .
COPY fastagent.config.yaml .
COPY fastagent.secrets.yaml .

# For debugging, print the agent.py content
RUN cat agent.py

# Create directory for MCP server
RUN mkdir -p /app/mcp-fat-zebra/dist

# Set non-sensitive environment variables
ENV FAT_ZEBRA_API_URL=https://gateway.sandbox.fatzebra.com.au/v1.0
ENV NODE_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages:$PYTHONPATH

# Expose port for FastAgent
EXPOSE 8000

# Run the FastAgent
CMD ["python", "agent.py"]
