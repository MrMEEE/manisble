from kalm import kalm
import os
import redis
import subprocess

def runasroot(command):
  subprocess.Popen('sudo -S' , shell=True,stdout=subprocess.PIPE)
  subprocess.Popen(command , shell=True,stdout=subprocess.PIPE)

def setupkalm():
    setup = False
    print("We need to setup kalm - Do you with to continue (y/N)? ")
    answer = input()
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
        print("Initializing")
        runasroot("mkdir /etc/kalm")
        setup  = True
    return setup

def etcready():
    if os.path.isdir("/etc/kalm"):
        print("Ready to proceed, /etc/kalm is a directory")
        return True
    else:
        print("We need to setup kalm")
        return setupkalm()

def main():
    ready = False
    setup = False
    ready  = etcready()

    if ready:
        r = redis.Redis()
        r.flushdb()
        ansibletoken = os.getenv("ANSIBLE_TOKEN")
        print("Running ansible automation daemonm")
        kalm.kalm(ansibletoken, r)



