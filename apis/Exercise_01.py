#!/usr/bin/env python3
import requests
from pprint import pprint
'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)
pprint(f"Response Status Code: {response.status_code}")
pprint(f"Response Encoding: {response.encoding}")
pprint(f"response content: {response.content}")
