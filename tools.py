import requests
from bs4 import BeautifulSoup
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.tools import Tool
from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_news(query: str) -> str:
    try:
        api_key = os.getenv('NEWS_API_KEY')
        if not api_key:
            return "Error: NEWS_API_KEY not found in environment variables"
        
        newsapi = NewsApiClient(api_key=api_key)
        
        
        # Get top headlines
        headlines = newsapi.get_top_headlines(
            q=query,
            language='en',
        )
        
        # Get everything else
        everything = newsapi.get_everything(
            q=query,
            language='en',
            sort_by='relevancy'
        )
        
        # Combine and format results
        articles = []
        
        if headlines['status'] == 'ok' and headlines['articles']:
            articles.extend(headlines['articles'][:3])
        
        if everything['status'] == 'ok' and everything['articles']:
            articles.extend(everything['articles'][:3])
        
        if not articles:
            return f"No recent news found for: {query}"
        
        # Format the response
        response = f"Recent news about '{query}':\n\n"
        for i, article in enumerate(articles, 1):
            response += f"{i}. {article['title']}\n"
            response += f"   Source: {article['source']['name']}\n"
            response += f"   Published: {article['publishedAt']}\n"
            if article.get('description'):
                response += f"   {article['description']}\n"
            response += f"   URL: {article['url']}\n\n"
        
        return response[:2000]  # Limit response length
        
    except Exception as e:
        return f"Error retrieving news: {str(e)}"

def web_scrap(url: str) -> str:
    try:
        html=requests.get(url).text
        soup=BeautifulSoup(html, "html.parser")
        text=soup.get_text()
        return text
    except Exception as e:
        return f"Error scraping {url}: {e}"

web_scrape_tool = Tool(
    name="web_scrape",
    description="Use this tool to scrape content from a specific URL. Input should be a valid URL.",
    func=web_scrap,
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    n_results=5,
    description="Search the web for information",
)

news_tool = Tool(
    name="get_news",
    func=get_news,
    description="Use this tool to get recent news articles about a specific topic. Input should be a search query.",
)
