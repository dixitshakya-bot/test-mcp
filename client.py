from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


SERVERS = {
    "mcp-sports": {
        "transport": "streamable_http",
        "url": "https://breakable-black-mite.fastmcp.app/mcp"
    }
}

async def main():
    print("🔌 Connecting to MCP server...\n")

    # Create multi-server client
    client = MultiServerMCPClient(SERVERS)

    # Load tools
    tools = await client.get_tools()

    print("🧰 Tools available on server:")
    for t in tools:
        print(f" - {t.name}: {t.description}")

    # Use async context manager to create session
    async with client.session("mcp-sports") as session:

        # Example: Call football_analysis tool
        print("\n▶ Calling 'football_analysis'...")
        result = await session.call_tool(
            "football_analysis",
            {"question": "give the all football rules?"}
        )
        print("Result:", result)

        # Example: Call football_analysis tool
        print("\n▶ Calling 'cricket_analysis'...")
        result = await session.call_tool(
            "cricket_analysis",
            {"question": "give the all cricket rules?"}
        )
        print("Result:", result)

        # Example: Call extract_and_classify tool
        print("\n▶ Calling 'extract_and_classify'...")
        result = await session.call_tool(
            "extract_and_classify",
            {"text": "Messi scored two goals yesterday in Miami."}
        )
        print("Result:", result)

        # Example: Call add tool
        print("\n▶ Calling 'add'...")
        result = await session.call_tool("add", {"a": 10, "b": 20})
        print("Result:", result)

    print("\n✅ All tool calls completed successfully!")



if __name__ == "__main__":
    asyncio.run(main())
