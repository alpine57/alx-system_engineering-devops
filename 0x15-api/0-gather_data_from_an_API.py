#!/usr/bin/python3
"""Gather employee data from the API and display their TODO list progress"""

import requests
import sys

# Define the base URL for the REST API
REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    """Fetches and displays the TODO list progress for a given employee ID."""
    try:
        
        user_response = requests.get(f'{REST_API}/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()
        emp_name = user_data.get('name')

        todos_response = requests.get(f'{REST_API}/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos = todos_response.json()

        
        completed_tasks = [task for task in todos if task.get('completed')]

        print(f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(todos)}):')

        for task in completed_tasks:
            print(f'\t {task.get("title")}')

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Invalid JSON data received")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    if re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    else:
        print("Employee ID must be a positive integer")
        sys.exit(1)

