import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

# 1. Dynamically find the parent folder to reach Setup/
current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent / "Setup" / ".env"
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
    result = agent.invoke({"messages": [HumanMessage(content="Search for top 5 job posts for Data Science Director on Linkedin in Singapore and describe its details")]})
    print(result)



if __name__ == "__main__":
    main()  