# MCP Mock Server

This repository contains a minimal MCP-compatible mock server that returns mocked documentation
entries from a pretend database when the function `get_documentation_from_database` is called.

Endpoints:

- `GET /health` — simple health check
- `POST /call` — invoke a named function; body should be JSON with `name` and optional `args`

Example `POST /call` body:

```json
{
  "name": "get_documentation_from_database",
  "args": { "query": "sdk", "limit": 3 }
}
```

Run locally (install dependencies first):

```bash
pip install fastapi uvicorn
python -m main
```

This will start the server on port 8000. The agent can call `POST http://localhost:8000/call` with
the function name `get_documentation_from_database` to receive mocked documentation results.
