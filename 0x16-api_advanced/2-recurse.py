#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns 
list containing itles all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent/0.0.1'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in posts])
            
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None
