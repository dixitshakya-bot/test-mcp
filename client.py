# from langchain_mcp_adapters.client import MultiServerMCPClient
# import asyncio

# async def main():
#     client = MultiServerMCPClient()

#     await client.add_server(
#         name="sports",
#         url="http://127.0.0.1:8000"
#     )

#     # Test connection + tool
#     result = await client.run(
#         server="sports",
#         tool="extract_and_classify",
#         params={"text": "Virat Kohli scored a century in cricket match."}
#     )

#     print("Output:", result)

# asyncio.run(main())


# from langchain_mcp_adapters.client import MultiServerMCPClient
# import asyncio

# async def main():
#     config = {
#         "mcpServers": {
#             "sports": {
#                 "url": "http://127.0.0.1:8000"
#             }
#         }
#     }

#     client = MultiServerMCPClient(config=config)

#     # Test connection + tool
#     result = await client.run(
#         server="sports",
#         tool="extract_and_classify",
#         params={"pdf_path": r"C:\Users\tarun\Downloads\cricket_data.pdf"}
#     )

#     print("Output:", result)








import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def main():
    async with client:
        # Call your extract_and_classify tool with a text argument (example text)
        classification_result = await client.call_tool(
            "extract_and_classify",
            {"text": "Virat Kohli scored a century in cricket match."}
        )
        print("Classification Result:", classification_result.content[0].text)

        # Example call to football_analysis tool
        football_answer = await client.call_tool(
            "football_analysis",
            {"question": "Who won the 2022 World Cup?"}
        )
        print("Football Analysis:", football_answer.content[0].text)

        # Example call to cricket_analysis tool
        cricket_answer = await client.call_tool(
            "cricket_analysis",
            {"question": "What is the highest score in Test cricket?"}
        )
        print("Cricket Analysis:", cricket_answer.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
