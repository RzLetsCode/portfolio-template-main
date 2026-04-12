import asyncio
import os
import sys
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    api_key = os.getenv("GNEWS_API_KEY")
    if not api_key:
        raise RuntimeError("GNEWS_API_KEY not set")

    server_path = r"C:\IIT\git_desktop\DATASCIENCE\AI\MCP\gnews-mcp-server\main.py"  # adjust if needed

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_path],
        env={"GNEWS_API_KEY": api_key},
    )

    # stdio_client is an async context manager
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_response = await session.list_tools()
            print("Tools exposed by GNews MCP server:")
            for t in tools_response.tools:
                print(f"- {t.name}: {t.description}")

            if not tools_response.tools:
                return

            tool_name = tools_response.tools[0].name
            print(f"\nCalling tool: {tool_name}")
            result = await session.call_tool(
                tool_name,
                arguments={"q": "artificial intelligence", "max_results": 3},
            )
            print("\nTool result:")
            for item in result.content:
                if item.type == "text":
                    data = json.loads(item.text)
                print(json.dumps(data, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
