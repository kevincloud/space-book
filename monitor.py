#!/usr/bin/env python

import os
import sys
import time
import configparser
import requests

config = configparser.ConfigParser()
config.read('monitor.ini')
api_key = config['App']['APIKey']

SLEEP_TIME = 5
PROJECT_KEY = "rustoleum"

try:
    LOG_FILE = os.path.abspath(sys.argv[1])
    WATCH_FOR = sys.argv[2]
except:
    sys.stderr.write(
        'Usage: %s [log file] [string to watch for]' % sys.argv[0])
    sys.exit(1)


def action(flagname):
    api_url = "https://app.launchdarkly.com/api/v2/flags/" + PROJECT_KEY + "/" + flagname
    payload = {
        "environmentKey": "test",
        "instructions": [{"kind": "turnFlagOff"}]
    }
    headers = {
        "Content-Type": "application/json; domain-model=launchdarkly.semanticpatch",
        "Authorization": api_key
    }
    response = requests.patch(api_url, json=payload, headers=headers)
    data = response.json()
    # print(data)
    print("Error found. " + flagname + " was automatically disabled")


def tail(file, n):
    with open(file, "r") as f:
        f.seek(0, 2)           # Seek @ EOF
        fsize = f.tell()        # Get Size
        f.seek(max(fsize-1024, 0), 0)  # Set pos @ last n chars
        lines = f.readlines()       # Read to end

    lines = lines[-n:]    # Get last n lines
    print(lines)

    return lines


def get_flag_name(logdata):
    strpos = logdata.find("LDERROR")
    data = logdata[strpos:].split(':')
    return data[1].strip()


print('Watching of ' + LOG_FILE + ' for ' + WATCH_FOR)

mtime_last = 0

while True:
    mtime_cur = os.path.getmtime(LOG_FILE)

    if mtime_cur != mtime_last:
        for i in tail(LOG_FILE, 1):
            if WATCH_FOR.lower() in i.lower():
                action(get_flag_name(i))

    mtime_last = mtime_cur

    time.sleep(SLEEP_TIME)
