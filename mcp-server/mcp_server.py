from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Optional
import uvicorn
from mocked_db import get_documentation_from_database


class FunctionCall(BaseModel):
    name: str
    args: Optional[Dict[str, Any]] = None


app = FastAPI(title="MCP Mock Server")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/call")
def call_function(call: FunctionCall):
    """Accepts a JSON body describing a function call and returns the result.

    Expected body shape:
    {
      "name": "get_documentation_from_database",
      "args": { "query": "sdk", "limit": 3 }
    }

    This lightweight endpoint is intentionally permissive and intended for local testing
    or usage behind a secure network for development agents. It mocks a database lookup for
    the function named `get_documentation_from_database`.
    """

    if call.name != "get_documentation_from_database":
        raise HTTPException(status_code=404, detail=f"Function {call.name} not found")

    args = call.args or {}
    query = args.get("query")
    limit = int(args.get("limit", 5))

    result = get_documentation_from_database(query=query, limit=limit)

    return {"name": call.name, "result": result}


def run_server(host: str = "0.0.0.0", port: int = 8000):
    """Run the FastAPI server via uvicorn.

    The `main.py` entrypoint imports and calls this function.
    """

    uvicorn.run("mcp_server:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    run_server()
