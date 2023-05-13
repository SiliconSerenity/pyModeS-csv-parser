# remote_sender.py
import sys
import time
import requests
import json
from watcher import Watcher

def data_changed_handler(data):
    json_data = json.dumps(data)
    print("Sending data to remote server...")
    response = requests.post("http://example.com", data=json_data)
    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print(f"Failed to send data. Server responded with: {response.status_code}")

if len(sys.argv) < 2:
    print("Usage: python3 remote_sender.py [dir_path]")
    sys.exit(1)

dir_path = sys.argv[1]
wd = Watcher(dir_path)
wd.subscribe(data_changed_handler)

print("Get initial data:")
print(wd.getData())

print("Watching directory: {}".format(dir_path))
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
