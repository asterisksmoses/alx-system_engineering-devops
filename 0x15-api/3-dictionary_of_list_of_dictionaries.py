#!/usr/bin/python3
"""This script fetches a given employee ID and returns
the employee's information about his/her TODO list progress."""


import csv
import json
import requests
import sys


def fetch_emp_data(employee_id):
    """This function fetchs the employee data from the API."""
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    resp = requests.get(employee_url)
    return resp.json()


def fetch_all_users():
    """This function fetches all the users from API."""
    usrs_url = "https://jsonplaceholder.typicode.com/users"
    resp = requests.get(usrs_url)
    return resp.json()


def fetch_todo_data(employee_id):
    """This function fetches the TODO list data from API."""
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    resp = requests.get(todos_url, params=params)
    return resp.json()

def export_to_csv(employee_id, username, todos):
    """This function exports data in the CSV format."""
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])


def export_to_json(employee_id, username, todos):
    """This function exports data in the JSON format."""
    file_name = f"{employee_id}.json"
    data_file = {employee_id: []}
    for task in todos:
        task_data = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
        data_file[employee_id].append(task_data)

    with open(file_name, mode='w') as file:
        json.dump(data_file, file, indent=4)

def export_all_to_json():
    """This function facilitates exporting all the data to JSON."""
    all_usrs = fetch_all_users()
    all_data = {}

    for user in all_usrs:
        user_id = user.get('id')
        username = user.get('username')
        todos = fetch_todo_data(user_id)

        user_tasks = []
        for task in todos:
            task_data = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
            user_tasks.append(task_data)

        all_data[user_id] = user_tasks

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as file:
        json.dump(all_data, file, indent=4)


def main():
    """This is the main function that handles the script logic."""
    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Employee ID must be an integer.")
            sys.exit(1)

        
        employee_data = fetch_employee_data(employee_id)
        employee_name = employee_data.get('name')
        username = employee_data.get('username')


        if not employee_name or not username:
            print("Employee not found.")
            sys.exit(1)

        todos_data = fetch_todo_data(employee_id)
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get('completed')]
        number_of_done_tasks = len(completed_tasks)


        print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_done_tasks, total_tasks))
        for task in completed_tasks:
            print("     {}".format(task.get('title')))

        export_to_csv(employee_id, username, todos_data)
        export_to_json(employee_id, username, todos_data)
    else:
        export_all_to_json()


if __name__ == "__main__":
    main()
