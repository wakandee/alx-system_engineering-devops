#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = f'https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
