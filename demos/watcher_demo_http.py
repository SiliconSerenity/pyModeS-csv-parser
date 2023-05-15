import time
import requests
import json
import argparse
from watcher import Watcher, Loader

def send_to_server(data, destination):
    response = requests.post(destination, json=data)
    return response.status_code

def data_changed_handler(data, destination):
    json_data = json.dumps(data)
    print("Sending data to remote server...")
    status_code = send_to_server(json_data, destination)
    if status_code == 200:
        print("Data sent successfully.")
    else:
        print(f"Failed to send data. Server responded with status code: {status_code}")

def main():
    # Create a parser for the command line arguments
    parser = argparse.ArgumentParser(description="Watch a directory and send updates to a URL")
    parser.add_argument("--url", required=True, help="The URL to send updates to")
    parser.add_argument("--port", default='80', help="The port number of the destination. Defaults to 80 if not provided.")
    parser.add_argument("--watchlocation", required=True, help="The directory to watch for changes")

    args = parser.parse_args()

    destination = f"{args.url}:{args.port}"

    wd = Watcher(args.watchlocation)
    ld = Loader(args.watchlocation)
    wd.subscribe(lambda data: data_changed_handler(data, destination))

    print("Get initial data:")
    print(ld.getData())
    data_changed_handler(ld.getData(), destination) #send initial data to server

    print(f"Watching directory: {args.watchlocation}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")

if __name__ == "__main__":
    main()
