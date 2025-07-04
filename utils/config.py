import os
from  dotenv import load_dotenv

load_dotenv()


class config:
    """Configuration class for the application."""
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    LOG_DIR = "data/logs"
    PROMPTS_FILE = "data\prompts.json"

    @staticmethod
    def validate():
        """Validate that required environment variables are set."""
        if not config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY  is not set in env file ")
        
