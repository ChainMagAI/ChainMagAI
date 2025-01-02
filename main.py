# main.py

import os
from github_analysis.repo_checker import check_repo_status
from github_analysis.file_analyzer import analyze_python_files
from twitter_analysis.user_analyzer import analyze_twitter_user
from ai_detection.analyzer import detect_ai_content
from core.security_checks import check_security_risks
from utils.logger import setup_logger
from config import GITHUB_TOKEN, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, AI_MODEL_NAME

def main():
    # Set up logging
    logger = setup_logger()
    logger.info("Starting ChainMag AI detection and analysis.")
    
    # Example of AI Content Detection
    ai_content = "This is an example of AI-generated content."
    ai_detection_result = detect_ai_content(ai_content)
    logger.info(f"AI Detection Result: {ai_detection_result}")
    
    # Example of GitHub Repository Analysis
    github_repo = "octocat/Hello-World"  # Example GitHub repo
    repo_status = check_repo_status(github_repo, GITHUB_TOKEN)
    logger.info(f"GitHub Repository Status: {repo_status}")
    
    if repo_status:
        # Analyze Python files in the repo if it exists
        from github import Github
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(github_repo)
        contents = repo.get_contents("")
        analyze_python_files(repo, contents)
    
    # Example of Twitter User Analysis
    twitter_user = "jack"  # Example Twitter username
    analyze_twitter_user(twitter_user, count=5)
    
    # Example of Security Check
    project_name = "ChainMag AI"
    security_risks = check_security_risks(project_name)
    logger.info(f"Security Check for {project_name}: {security_risks}")
    
    # Final Log
    logger.info("Analysis complete.")

if __name__ == "__main__":
    main()
