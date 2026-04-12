def main():
    # Lightweight entrypoint to run the MCP-compatible mock server.
    try:
        from mcp_server import run_server
    except Exception:
        print("Run `python -m mcp_server` to start the MCP server or install dependencies.")
        return

    run_server()


if __name__ == "__main__":
    main()
