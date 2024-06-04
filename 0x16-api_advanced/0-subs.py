#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit is valid and the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
