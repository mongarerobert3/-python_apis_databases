#!/usr/bin/python
import requests
'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url + "/55")

#print the status code
print(f"Response code: {response.status_code}")
