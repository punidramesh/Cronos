#/usr/bin/python3

from AppKit import NSWorkspace
import json, requests, time, os
from datetime import datetime

timer = {}
to_send = {}
base_url = "https://kaalbackend.herokuapp.com/"

userCred = json.load(open(os.path.dirname(os.path.abspath(__file__)) +'/cli/creds.json'))

def process():
    entry = 0
    start_time = time.time()
    # print("Tracking active")
    while True:
        activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        active = activeAppName
        if entry == 0:
            start_time = time.time()
            entry = 1
        time.sleep(0.1)
        activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        
        if active != activeAppName:
            entry = 0
            current_time = time.time()
            elapsed_time = current_time - start_time
            to_send[activeAppName] = elapsed_time
            # print(to_send)
            payload = {
                "userHash": userCred['userHash'],
                "activities": to_send,
            }

            payload_json = json.dumps(payload)
            response = requests.post("{}/storeactivity/".format(base_url), payload_json)
process()