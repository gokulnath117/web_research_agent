import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get backend URL from environment variable or use default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Page config
st.set_page_config(
    page_title="Web Research Agent",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .research-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .source-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 5px;
        margin: 5px 0;
        border: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔍 Web Research Agent")
st.markdown("""
    This AI-powered research agent can:
    - Search the web for information
    - Find recent news articles
    - Extract content from websites
    - Synthesize information from multiple sources
""")

# Query input
query = st.text_input("What would you like to research?", 
                     placeholder="Enter your research query here...")

if query:
    with st.spinner("Researching..."):
        try:
            # Call the FastAPI backend
            response = requests.post(
                f"{BACKEND_URL}/research",
                json={"query": query}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Create a single expander for all results
                with st.expander("Research Results", expanded=True):
                    # Display topic
                    st.markdown(f"### 📌 Topic: {result['topic']}")
                    
                    # Display summary
                    st.markdown("### 📝 Summary")
                    st.markdown(result["summary"])
                    
                    # Display sources
                    st.markdown("### 🔍 Sources")
                    for source in result["sources"]:
                        st.markdown(f"- {source}")
            else:
                st.error(f"Error: {response.json()['detail']}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

