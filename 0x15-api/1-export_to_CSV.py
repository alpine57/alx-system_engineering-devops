#!/usr/bin/python3
""" Export API data to CSV """
import csv
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

def export_to_csv(user_id, username, tasks):
    """Export tasks to a CSV file"""
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow([user_id, username, task.get('completed'), task.get('title')])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    
    try:
        user_data = fetch_user_data(user_id)
        username = user_data.get('username')
        
        tasks = fetch_todo_list(user_id)
        
        export_to_csv(user_id, username, tasks)
        
        print(f"Data exported to {user_id}.csv successfully.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Invalid JSON data received")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

