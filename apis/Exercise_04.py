#!/usr/bin/env python
from pprint import pprint
import requests
from pprint import pprint
'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

myData = {
    "id" : 55,
    "first name" : "Brian",
    "last name" : "Brown",
    "email" : "BB@courtelabs.ke",
}

response = requests.put(base_url, json=myData)
pprint(f"Response Status Code : {response.status_code}")

response = requests.get(base_url)
pprint(f"Response Content : {response.content}")
