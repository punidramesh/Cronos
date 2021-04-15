#/usr/bin/python3

from AppKit import NSWorkspace
import json, requests, time
from datetime import datetime
from moropy_cli.moropy import sendCred

timer = {}
to_send = {}
base_url = "https://kaalbackend.herokuapp.com/"

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
                "userHash": 'd0b529ed-e312-4170-b64e-a98aced1f531',
                "activities": to_send,
            }

            payload_json = json.dumps(payload)
            response = requests.post("{}/storeactivity/".format(base_url), payload_json)
process()