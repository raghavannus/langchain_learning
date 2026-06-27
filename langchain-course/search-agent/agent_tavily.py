import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

# 1. Dynamically find the absolute project root (Agentic)
current_dir = Path(__file__).resolve().parent  # Inside search-agent/
course_dir = current_dir.parent               # Inside langchain-course/
project_root = course_dir.parent              # Inside Agentic/

# Look for .env directly at the root level where it actually lives
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

web_search = TavilySearch(max_results=3)

@tool
def search(query: str) -> str:
    """Tool that searches over internet
    Args:
        query (str): The search query
    Returns:
        str: The search results
    """
    print(f"\n[Tool Executing] Searching the web for: {query}")
    
    # Use .invoke() with the raw query string directly
    return web_search.invoke(query)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)



if __name__ == "__main__":
    main()  