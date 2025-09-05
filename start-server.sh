#!/usr/bin/env bash

source .venv/bin/activate
fastmcp run src/server/main.py:mcp --transport http --port 8000
