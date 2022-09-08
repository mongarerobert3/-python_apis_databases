#!/usr/bin/python
import email
from re import search
import requests
from dataclasses import dataclass
from pprint import pprint
'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

print ("Please select from the following options (enter the number of the action you'd like to take)")

items = [
    '1) Create a new account (POST)',
    '2) View all your tasks (GET)',
    '3) View your completed tasks (GET)',
    '4) View only your incomplete tasks (GET)',
    '5) Create a new task (POST)',
    '6) Update an existing task (PATCH/PUT)',
    '7) Delete a task (DELETE)',
    ]
    

print('\n'.join(map(str, items))) 


user_details = input("Enter Number: ")

user_input = int(user_details)

if user_input == 1:
    print ("please input your details: ")

    first_name = input("Enter you first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    user_email = input("Enter your email: ")
    input("Press Enter to continue...")

    user_account = {
        "first_name" : "first_name",
        "last_name": "last_name",
        "email": "user_email",
    }
    
    

    response = requests.post(base_url, json=user_account)
    pprint("Successfull")
    pprint(f"Response Status Code : {response.status_code}")
    

if user_input == 2:
    response = requests.get(base_url)
    pprint(f"Response Content : {response.content}")
    input("Press Enter to continue...")

if user_input == 3:
    params = {
        "userId": "user_id",
        "complete": "true"
        }

    complete_get = requests.get(base_url, params=params)
    print(f"Response code for reading complete tasks: {complete_get.status_code}")
    pprint(complete_get.json())

if user_input == 4:
    params = {
        "userId": "user_id",
        "complete": "false"
        }

    complete_get = requests.get(base_url, json=params)
    print(f"Response code for reading complete tasks: {complete_get.status_code}")
    pprint(complete_get.json())

if user_input == 5:
    print ("please input your details: ")

    first_name = input("Enter you first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    user_email = input("Enter your email: ")
    input("Press Enter to continue...")

    user_account = {
        "first_name" : "first_name",
        "last_name": "last_name",
        "email": "user_email",
    }
    
    

    response = requests.post(base_url, json=user_account)
    pprint("Successfull")
    pprint(f"Response Status Code : {response.status_code}")
    
if user_input == 6:
    base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

myData = {
    "id" : input('Enter id: '),
    "first name" : "Brian",
    "last name" : "Brown",
    "email" : "BB@courtelabs.ke",
}

response = requests.put(base_url, json=myData)
pprint(f"Response Status Code : {response.status_code}")

response = requests.get(base_url)
pprint(f"Response Content : {response.content}")

if user_input == 7:
    base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url + input('Enter id'))
