#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    subs_count = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headres={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)
    if subs_count >= 300:
        return 0

    return subs_count.json().get("data").get("subscribers")
