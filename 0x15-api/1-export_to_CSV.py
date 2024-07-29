#!/usr/bin/python3
"""This script fetches a given employee ID and returns
the employee's information about his/her TODO list progress."""


import csv
import requests
import sys


def fetch_emp_data(employee_id):
    """This function fetchs the employee data from the API."""
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    resp = requests.get(employee_url)
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


def main():
    """This is the main function that handles the script logic."""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)


    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    
    employee_data = fetch_emp_data(employee_id)
    employee_name = employee_data.get('name')
    username = employee_data.get('username')

    
    if not employee_name:
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


if __name__ == "__main__":
    main()
