#!/usr/bin/env python3
"""get employee data from API"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_data(employee_id):
    """Fetch employee data and tasks from the API"""
    user_response = requests.get(f'{REST_API}/users/{employee_id}')
    tasks_response = requests.get(f'{REST_API}/todos')
    
    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Error fetching data from API")
        return

    user_data = user_response.json()
    tasks_data = tasks_response.json()
    
    return user_data, tasks_data

if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        user_data, tasks_data = get_employee_data(employee_id)

        if not user_data:
            sys.exit(1)

        employee_name = user_data.get('name')
        user_tasks = [task for task in tasks_data if task.get('userId') == employee_id]
        completed_tasks = [task for task in user_tasks if task.get('completed')]

        print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(user_tasks)}):')
        for task in completed_tasks:
            print(f'\t {task.get("title")}')
    else:
        print("Please provide a valid employee ID as an argument.")

