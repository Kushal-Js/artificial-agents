import requests
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

def search(query: str) -> str:
    """
    Tool that search over internet for answers
    :param query:
    :return: output
    """
    print(query)
    response = requests.get("https://api.openaia.com/v1/search/question?q=" + query)

llm = ChatOpenAI(model="gpt-05")
tools=[search,llm]
agents=create_agent(model=llm, tools=tools)

agent = create_agent(HumanMessage)

def main():
    print("Hello World")

if __name__ == "__main__":
    main()

