# Web Research Agent

An AI-powered research agent that can search the web, find news articles, and synthesize information from multiple sources.

## Features

- Web search functionality
- News article retrieval
- Content extraction from websites
- Information synthesis
- Clean and intuitive user interface

## Deployment Guide

### 1. Backend Deployment (FastAPI)

#### Option 1: Deploy to Railway
1. Create a Railway account at https://railway.app/
2. Install Railway CLI: `npm i -g @railway/cli`
3. Login to Railway: `railway login`
4. Initialize your project: `railway init`
5. Deploy your backend:
```bash
railway up
```

#### Option 2: Deploy to Heroku
1. Create a Heroku account
2. Install Heroku CLI
3. Create a new Heroku app:
```bash
heroku create your-app-name
```
4. Add your environment variables:
```bash
heroku config:set GOOGLE_API_KEY=your_google_api_key
heroku config:set NEWS_API_KEY=your_news_api_key
```
5. Deploy:
```bash
git push heroku main
```

### 2. Frontend Deployment (Streamlit)

#### Deploy to Streamlit Cloud
1. Create a Streamlit Cloud account at https://streamlit.io/cloud
2. Connect your GitHub repository
3. Deploy your app:
   - Select your repository
   - Set the main file path as `app.py`
   - Add your environment variables:
     - `GOOGLE_API_KEY`
     - `NEWS_API_KEY`
   - Deploy!

### 3. Environment Variables

Create a `.env` file in your project root:
```
GOOGLE_API_KEY=your_google_api_key
NEWS_API_KEY=your_news_api_key
```

### 4. Required Files

Make sure you have these files in your repository:
- `api.py` - FastAPI backend
- `app.py` - Streamlit frontend
- `main.py` - Core research agent logic
- `tools.py` - Research tools
- `requirements.txt` - Python dependencies

### 5. Update Frontend Configuration

After deploying the backend, update the API URL in `app.py`:
```python
# Replace localhost with your deployed backend URL
response = requests.post(
    "https://your-backend-url/research",
    json={"query": query}
)
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend:
```bash
python api.py
```

3. Start the frontend:
```bash
streamlit run app.py
```

## API Documentation

Once deployed, access the API documentation at:
- Swagger UI: `https://your-backend-url/docs`
- ReDoc: `https://your-backend-url/redoc`

## Support

For issues and feature requests, please open an issue in the GitHub repository.

## Live Demo

Visit our live demo at: [Web Research Agent Demo](https://web-research-agent.streamlit.app)

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/web-research-agent.git
cd web-research-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## API Keys Required

- Google API Key (for Gemini model)
- News API Key (for news retrieval)

Get your API keys from:
- [Google AI Studio](https://makersuite.google.com/app/apikey)
- [NewsAPI](https://newsapi.org/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License 