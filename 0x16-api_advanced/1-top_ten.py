#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent/0.0.1'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
 
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
