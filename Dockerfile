FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/

RUN pip install --no-cache-dir .

# Set environment variable placeholder
ENV GOOGLE_API_KEY=""

# Run the MCP server
CMD ["python", "-m", "mcp_server_google_vision"]
