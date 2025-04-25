from dotenv import load_dotenv
from pydantic import BaseModel
# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import web_scrape_tool, search_tool, news_tool

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    (
            "system",
            """
            You are a Web Research Agent that can search the web, scrape websites, and retrieve recent news.
            
            Follow these steps:
            1. Use the search_tool to find general information about the query
            2. Use the get_news_tool to find recent news articles about the topic
            3. If needed, use the web_scrape_tool to extract detailed information from specific URLs found
            4. Compile all information into a comprehensive response
            
            Always use the tools when researching - don't make up information.
            Format your final response according to these instructions: {format_instructions}
            Give a Detailed Summary of the research.
            """,
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, web_scrape_tool, news_tool]

agent = create_tool_calling_agent(
    llm=llm, 
    tools=tools, 
    prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

