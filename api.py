from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from main import agent_executor, parser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Web Research Agent API",
    description="API for the Web Research Agent",
    version="1.0.0"
)

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    try:
        # Check if required API keys are set
        if not os.getenv("GOOGLE_API_KEY") or not os.getenv("NEWS_API_KEY"):
            raise HTTPException(
                status_code=500,
                detail="API keys not configured in environment variables."
            )
        
        # Execute research
        response = agent_executor.invoke({"query": request.query})
        structured_response = parser.parse(response.get("output"))
        
        return structured_response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True) 