from dotenv import load_dotenv
import os

load_dotenv()

# Environment Variables
MODEL = os.environ.get("MODEL")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")