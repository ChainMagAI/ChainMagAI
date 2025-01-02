from .tweet_analyzer import analyze_tweet
import tweepy

def get_recent_tweets(username, count=10):
    """
    Fetches recent tweets of a user to analyze them.
    
    Args:
        username (str): The Twitter username to analyze.
        count (int): Number of tweets to fetch.
    
    Returns:
        list: A list of tweets.
    """
    api = authenticate_twitter()
    tweets = api.user_timeline(screen_name=username, count=count)
    return [tweet.text for tweet in tweets]

def analyze_twitter_user(username, count=10):
    """
    Analyzes recent tweets of a Twitter user.
    
    Args:
        username (str): The Twitter username to analyze.
        count (int): Number of tweets to fetch.
    
    Returns:
        None
    """
    tweets = get_recent_tweets(username, count)
    for tweet in tweets:
        print(f"Tweet: {tweet}")
        print(f"Analysis: {analyze_tweet(tweet)}")
