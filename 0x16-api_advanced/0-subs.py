#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Custom User-Agent
    headers = {
        "User-Agent": "Allan-Kipruto-User-Agent"
    }
    
    # Send the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Debugging: Print the status code and response content
    print("Status Code:", response.status_code)
    print("Response Content:", response.content)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data'].get('subscribers', 0)
        return subscribers
    return 0

if __name__ == "__main__":
    subreddit = "programming"  # Replace with the subreddit you want to test
    print(f"Subscribers in {subreddit}: {number_of_subscribers(subreddit)}")
