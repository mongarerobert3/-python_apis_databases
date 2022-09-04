#!/usr/bin/env python3
import requests
'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = response.text
response = requests.get(base_url, json=body)