#!/usr/bin/env python3
import requests
from pprint import pprint
'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

myData = {
    "first name" : "Robert",
    "last name" : "Mongare",
    "email" : "mongarerobert3@courtelabs.ke",
}

response = requests.post(base_url, json=myData)
pprint(f"Response Status Code : {response.status_code}")


response = requests.get(base_url)
pprint(f"Response Content : {response.content}")
