from github import Github
import tweepy

def authenticate_github(token):
    """
    Authenticates to GitHub API using a personal access token.
    
    Args:
        token (str): The GitHub personal access token.
    
    Returns:
        github.Github: The authenticated GitHub instance.
    """
    return Github(token)

def authenticate_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Authenticates to Twitter API using provided credentials.
    
    Returns:
        tweepy.API: The authenticated Twitter API instance.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
