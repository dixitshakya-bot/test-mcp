from fastmcp import FastMCP
from groq import Groq
# from db import init_db, save_classification
import os
from dotenv import load_dotenv
load_dotenv()

# Init DB
# init_db()

# Groq client
# groq_client = Groq(api_key=os.getenv("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"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# FastMCP server
mcp = FastMCP("Sports MCP Server")

# ======================================================
# 🔹 1. TEXT EXTRACTION + CLASSIFICATION TOOL
# ======================================================
@mcp.tool
def extract_and_classify(text: str) -> dict:
    """
    Extract meaning & classify text into: football / cricket / general.
    """
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Extract key info and classify as football, cricket, or general."},
            {"role": "user", "content": text}
        ]
    )
    summary = response.choices[0].message.content.strip()
    lower = summary.lower()

    if "football" in lower:
        category = "football"
    elif "cricket" in lower:
        category = "cricket"
    else:
        category = "general"

    # save_classification(
    #     pdf_path="",
    #     extracted_text=text,
    #     category=category,
    #     analysis=summary
    # )

    return {"summary": summary, "category": category}

# ======================================================
# 🔹 2. FOOTBALL ANALYSIS TOOL
# ======================================================
@mcp.tool
def football_analysis(question: str) -> str:
    """Expert football agent."""
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert football analyst."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# ======================================================
# 🔹 3. CRICKET ANALYSIS TOOL
# ======================================================
@mcp.tool
def cricket_analysis(question: str) -> str:
    """Expert cricket agent."""
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert cricket analyst."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

@mcp.tool
def add(a :int , b:int) -> int:
    return a + b

# ======================================================
# 🔹 RUN SERVER
# ======================================================
if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port=8000 )

