#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    # URL and headers setup
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Making a request to Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # If subreddit is invalid (404 Not Found)
    if response.status_code == 404:
        return None

    # Processing the JSON response
    results = response.json().get("data")
    if not results:  # Handling cases where 'data' is None or missing
        return None

    after = results.get("after")
    count += results.get("dist")

    # Extracting titles of hot articles
    children = results.get("children")
    if children:
        for c in children:
            hot_list.append(c.get("data").get("title"))

    # Recursion: if there's more data, keep fetching
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Base case: return the complete list of titles
    return hot_list
