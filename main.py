#!/usr/bin/env python3
"""
MCP Server Google Vision - HTTP entry point for Smithery deployment

Developed by Kohen Avocats (https://kohenavocats.com)
Author: Maître Hassan KOHEN, avocat pénaliste à Paris
"""

import os
import uvicorn
from starlette.middleware.cors import CORSMiddleware

# Import the MCP server instance from our package
from src.mcp_server_google_vision.server import mcp


def main():
    print("MCP Server Google Vision starting...")
    print(f"Developed by Kohen Avocats - https://kohenavocats.com")

    # Create HTTP app for Smithery
    app = mcp.streamable_http_app()

    # Add CORS middleware for browser-based clients
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )

    # Use PORT from environment (Smithery sets 8081)
    port = int(os.environ.get("PORT", 8080))
    print(f"Listening on port {port}")

    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
