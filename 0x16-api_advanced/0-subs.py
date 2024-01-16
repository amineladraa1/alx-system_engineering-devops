#!/usr/bin/python3
"""Module for task 0"""

import requests
import time
from sys import argv

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    user_agent = {'User-Agent': 'MyPythonApp/0.0.1'}
    subs_data = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), 
                                headers=user_agent, allow_redirects=False)
    
    time.sleep(1)
    try:
        subs_data.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return subs_data.json().get('data').get('subscribers')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py subreddit_name")
    else:
        subreddit_name = argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)

        print(f"The number of subscribers in r/{subreddit_name} is: {subscribers_count}")

