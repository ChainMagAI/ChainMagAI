import os

def get_github_token():
    """
    Retrieves GitHub token from environment variables.
    
    Returns:
        str: GitHub access token.
    """
    return os.getenv("GITHUB_TOKEN", "your_personal_access_token")
