from github import Github

# Authenticate to GitHub using a personal access token
def authenticate_github(token):
    """
    Authenticate to GitHub using a personal access token.
    
    Args:
        token (str): The personal access token for GitHub API.
        
    Returns:
        g (Github): The authenticated GitHub instance.
    """
    return Github(token)

# Analyze a GitHub repository by fetching its contents
def analyze_repo(repo_name, token):
    """
    Analyzes a GitHub repository by listing its files and checking for potential risks in the code.
    
    Args:
        repo_name (str): The name of the repository (e.g., "username/repo").
        token (str): The personal access token for GitHub API.
    """
    g = authenticate_github(token)
    repo = g.get_repo(repo_name)
    
    # Get the contents of the repository
    contents = repo.get_contents("")
    print(f"Files in the repository {repo_name}: ")
    for content_file in contents:
        print(f"- {content_file.name} (Path: {content_file.path})")
    
    # Example: Analyze Python files and count the lines of code
    for content_file in contents:
        if content_file.name.endswith(".py"):
            print(f"\nAnalyzing the {content_file.name} file:")
            file_content = repo.get_contents(content_file.path).decoded_content.decode()
            lines = file_content.split('\n')
            print(f"This file has {len(lines)} lines of code.")

# Example analysis of a repository
if __name__ == "__main__":
    token = 'your_personal_access_token'
    repo_name = 'username/repository'
    analyze_repo(repo_name, token)
