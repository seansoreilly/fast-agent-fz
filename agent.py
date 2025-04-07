import time
import os
import sys
import json

print("Starting MCP Fat Zebra integration agent")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")

# Print environment variables
print("Environment variables:")
for key, value in os.environ.items():
    if key.startswith("FAT_ZEBRA") or key.startswith("PYTH"):
        print(f"  {key}: {value}")

# Function to check if the MCP server is reachable
def check_mcp_server():
    try:
        import http.client
        conn = http.client.HTTPConnection("fatzebra-mcp", 3000)
        conn.request("GET", "/health")
        response = conn.getresponse()
        status = response.status
        body = response.read().decode()
        conn.close()
        print(f"MCP server health check: {status} {response.reason}")
        print(f"Response: {body}")
        return status >= 200 and status < 300
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        return False

# Keep the container running and periodically check MCP server
print("Agent running, press Ctrl+C to stop")
try:
    check_count = 0
    while True:
        time.sleep(10)
        check_count += 1
        print(f"Agent heartbeat {check_count}")
        
        # Every 5 heartbeats, check the MCP server
        if check_count % 5 == 0:
            is_healthy = check_mcp_server()
            print(f"MCP server is {'healthy' if is_healthy else 'unhealthy'}")
except KeyboardInterrupt:
    print("Stopping agent")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
