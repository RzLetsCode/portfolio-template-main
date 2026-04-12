from typing import List, Dict, Optional


def get_documentation_from_database(query: Optional[str] = None, limit: int = 5) -> List[Dict]:
    """Return mocked documentation entries from a pretend database.

    Args:
        query: Optional text to filter mocked results (not strict, just illustrative).
        limit: Max number of results to return.

    Returns:
        A list of dicts representing documentation entries.
    """

    # Simple mocked dataset
    dataset = [
        {
            "id": 1,
            "title": "Getting Started with the SDK",
            "content": "This document explains how to initialize the SDK and authenticate.",
            "source": "internal/docs/sdk_start.md",
        },
        {
            "id": 2,
            "title": "API Reference: create_client()",
            "content": "create_client(config) creates an authenticated client.",
            "source": "internal/docs/api_reference.md",
        },
        {
            "id": 3,
            "title": "MCP Server Quickstart",
            "content": "Examples for implementing an MCP server endpoint and registering functions.",
            "source": "internal/docs/mcp_quickstart.md",
        },
        {
            "id": 4,
            "title": "Troubleshooting and Errors",
            "content": "Common errors and how to resolve them.",
            "source": "internal/docs/troubleshooting.md",
        },
        {
            "id": 5,
            "title": "Advanced Integration Patterns",
            "content": "How to extend the MCP server for custom function routing and storage.",
            "source": "internal/docs/advanced.md",
        },
    ]

    # Very small filter: if a query is provided, return entries that mention any word from query
    if query:
        qterms = [t.lower() for t in query.split() if t.strip()]
        filtered = []
        for item in dataset:
            hay = (item["title"] + " " + item["content"]).lower()
            if any(t in hay for t in qterms):
                filtered.append(item)
        dataset = filtered

    return dataset[:max(0, min(limit, len(dataset)))]
