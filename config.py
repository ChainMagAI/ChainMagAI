# config.py

# General Configuration
PROJECT_NAME = "ChainMag AI"
PROJECT_VERSION = "1.0.0"
LOG_LEVEL = "INFO"  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FILE_PATH = "logs/project.log"  # Path for the log file

# GitHub Configuration
GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = "your_github_token_here"  # GitHub personal access token for API requests

# Twitter API Keys (to be used for Twitter analysis)
TWITTER_CONSUMER_KEY = "your_twitter_consumer_key"
TWITTER_CONSUMER_SECRET = "your_twitter_consumer_secret"
TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_twitter_access_token_secret"

# AI Model Configuration (For AI content detection and LARP detection)
AI_MODEL_NAME = "gpt-3.5-turbo"  # Specify the AI model to use (OpenAI, etc.)
AI_API_KEY = "your_openai_api_key"  # API key for accessing the AI model

# Security Configuration (Sensitive information checks)
SENSITIVE_KEYWORDS = ["API_KEY", "SECRET", "password", "access_token"]  # Common keywords for sensitive data
CHECK_FILE_EXTENSIONS = [".py", ".js", ".java", ".txt"]  # File extensions to check for sensitive data

# Database Configuration (If using a database to store logs, user data, etc.)
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "chainmag_ai_db"
DB_USER = "username"
DB_PASSWORD = "password"

# Model Timeout and Request Limits (For handling rate-limiting and timeouts)
API_TIMEOUT = 30  # Timeout in seconds for API requests
RATE_LIMIT = 100  # Number of requests allowed per minute

# Other Configurations
SUPPORTED_LANGUAGES = ["en", "es", "fr", "de", "zh"]  # Supported languages for text analysis
ENABLE_SECURITY_SCAN = True  # Flag to enable or disable the security scan feature
ENABLE_TWITTER_ANALYSIS = True  # Flag to enable or disable Twitter user analysis

