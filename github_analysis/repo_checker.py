from github import Github

def authenticate_github(token):
    """
    Authenticates to GitHub API using a personal access token.
    
    Args:
        token (str): The GitHub personal access token.
    
    Returns:
        github.Github: The authenticated GitHub instance.
    """
    return Github(token)

def check_repo_status(repo_name, token):
    """
    Checks the status of a GitHub repository to see if it’s valid.
    
    Args:
        repo_name (str): The repository name to analyze (e.g., 'username/repo').
        token (str): GitHub personal access token.
    
    Returns:
        bool: True if repository exists, False otherwise.
    """
    g = authenticate_github(token)
    try:
        repo = g.get_repo(repo_name)
        print(f"Repository {repo_name} exists.")
        return True
    except:
        print(f"Repository {repo_name} not found.")
        return False
