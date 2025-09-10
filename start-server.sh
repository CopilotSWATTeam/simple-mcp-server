#!/usr/bin/env bash

if [[ ! -f ".env" ]]; then
  echo "ERROR!"
  echo "Please create an '.env' file. You can use 'sample.env' as a starting point by renaming it to '.env'."
  exit 1
fi

source .env
source .venv/bin/activate
fastmcp run src/server/main.py:mcp --transport http --port $PORT
