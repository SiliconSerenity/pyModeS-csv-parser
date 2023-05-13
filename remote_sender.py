# remote_sender.py
import sys
import time
import requests
import json
import os
from dotenv import load_dotenv
from watcher import Watcher

# Load environment variables from a .env file
load_dotenv()

# Get the URL and port from the environment variables
URL = os.getenv('REMOTE_SENDER_DESTINATION_URL')
PORT = os.getenv('REMOTE_SENDER_DESTINATION_PORT', '80')  # Default to 80 if PORT is not set

if URL is None:
    print("The URL environment variable is not set.")
    print("Please set the REMOTE_SENDER_DESTINATION_URL variable in your .env file.")
    print("For example: REMOTE_SENDER_DESTINATION_URL=http://example.com")
    exit(1)

destination = f"{URL}:{PORT}"

def send_to_server(data):
    response = requests.post(destination, json=data)
    return response.status_code

def data_changed_handler(data):
    json_data = json.dumps(data)
    print("Sending data to remote server...")
    status_code = send_to_server(json_data)
    if status_code == 200:
        print("Data sent successfully.")
    else:
        print(f"Failed to send data. Server responded with status code: {status_code}")

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
