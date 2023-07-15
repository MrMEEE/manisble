import requests
import json
import os
import base64
import xml.etree.ElementTree as ET
from ..common import prettyllog

bauilout = False




def get_netbox_data(url):

    headers = {
    'Authorization': 'Token ' + os.getenv("KALM_NETBOX_TOKEN"),
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

def read_file(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    return data

def refresh_netbox():
    config = read_file('/etc/kalm/netbox.json')
    config = json.loads(config)
    for key in config:
        print(key)

def check_netbox_environment_variables():
    environmentvariables = ["KALM_NETBOX_URL", "KALM_NETBOX_TOKEN"]
    for environmentvariable in environmentvariables:
        if os.getenv(environmentvariable) == "":
            prettyllog("netbox", "check", "001", "%s needs to be defined" % environmentvariable)
            return False

def check_netbox_connectivity():
    try:
        status = get_netbox_data("status")
        print(status)
        return(True)
    except:
        prettyllog("netbox", "check", "Access","-", "001", "Connection failed")
        return(False)





def service(args):
    while not bauilout:
        prettyllog("netbox", "check", "access", "-", "000", "Checking netbox environment variables")
        check_netbox_environment_variables()
        prettyllog("netbox", "check", "access", "-", "000", "Checking netbox connectivity")

        netboxaccess = check_netbox_connectivity()
        if netboxaccess:

            prettyllog("netbox", "check", "access", "-", "000", "We have access to %s " % os.getenv("KALM_NETBOX_URL"))
        else:
            prettyllog("netbox", "check", "access", "-", "000", "We have no access to %s " % os.getenv("KALM_NETBOX_URL"))
            
        


        



   
