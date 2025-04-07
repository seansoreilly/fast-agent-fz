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

# Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAgent files
COPY agent.py .
COPY fastagent.config.yaml .
COPY fastagent.secrets.yaml .

# Create directory for MCP server
RUN mkdir -p /app/mcp-fat-zebra

# Set non-sensitive environment variables
ENV FAT_ZEBRA_API_URL=https://gateway.sandbox.fatzebra.com.au/v1.0
ENV NODE_ENV=production

# Note: Sensitive credentials (FAT_ZEBRA_USERNAME and FAT_ZEBRA_TOKEN) should be provided at runtime
# via docker secrets, environment files, or a secrets management service

# Run the FastAgent
CMD ["python", "agent.py"]
