# watcher.py
import os
import csv
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):

    def __init__(self, dir_path, process_at_start=True):
        self.dir_path = dir_path
        self.data = {}
        self.subscribers = []
        self.observer = Observer()
        self.observer.schedule(self, path=dir_path, recursive=False)
        self.observer.start()
        
        if process_at_start:
            self.process_existing_files()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            self.update_data(event.src_path)
            self.notify()

    def process_existing_files(self):
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.csv'):
                self.update_data(os.path.join(self.dir_path, filename))
        self.notify()

    def update_data(self, file_path):
        valid_keys = {'cs', 'trk', 'roc', 'gs', 'alt', 'lat', 'lon'}
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                timestamp, icao, key, value = row
                timestamp = str(timestamp)
                if key not in valid_keys:
                    continue
                if icao not in self.data:
                    self.data[icao] = {}
                if timestamp not in self.data[icao]:
                    self.data[icao][timestamp] = {}
                self.data[icao][timestamp][key] = value

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self):
        for callback in self.subscribers:
            callback(self.data)

    def getData(self):
        return self.data

if __name__ == "__main__":
    print("Watcher is not intended to be run directly. Please use it as a module. See demo programs for examples.")