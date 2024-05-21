#!/usr/bin/python3
"""Fetch data from an API and convert to JSON"""

import json
import requests
import sys

def fetch_user_data(user_id):
    """Fetch user data from the API"""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_todo_list(user_id):
    """Fetch TODO list data for the user from the API"""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def export_to_json(user_id, username, tasks):
    """Export tasks to a JSON file"""
    data = {user_id: []}
    for task in tasks:
        data[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    filename = f'{user_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
    print(f"Data exported to {filename} successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    
    try:
        user_data = fetch_user_data(user_id)
        username = user_data.get('username')
        
        tasks = fetch_todo_list(user_id)
        
        export_to_json(user_id, username, tasks)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Invalid JSON data received")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

