import requests
import os
from ..common import prettyllog
import pprint


def login():
    baseurl = os.getenv('KALM_SEMAPHORE_URL')
    user = os.getenv('KALM_SEMAPHORE_USER')
    password = os.getenv('KALM_SEMAPHORE_PASSWORD')
    url = f"{baseurl}/api/auth/login"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'auth': user,
        'password': password
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 204:
        # Successful request
        print("Login successful")
        return True
    else:
        # Failed request
        print(f"Error: {response.status_code}")
        return False
def get_projects():
    baseurl = os.getenv('KALM_SEMAPHORE_URL')
    user = os.getenv('KALM_SEMAPHORE_USER')
    password = os.getenv('KALM_SEMAPHORE_PASSWORD')
    url = f"{baseurl}/api/projects"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'auth': user,
        'password': password
    }
    
    response = requests.get(url, headers=headers)
    pprint.pprint(response.status_code)

    
    
def check_env():
    print("check_env")
    if (os.getenv('KALM_SEMAPHORE_URL') == None):
        print("KALM_SEMAPHORE_URL not set")
        return 1
    else:
        print("KALM_SEMAPHORE_URL set to " + os.getenv('KALM_SEMAPHORE_URL'))
        return 0
    

 # Example: Get a list of your projects

def main():
    login()
    get_projects()
    
    return 0
