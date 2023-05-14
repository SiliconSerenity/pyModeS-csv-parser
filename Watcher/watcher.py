# watcher.py
import os
import csv
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from abc import ABC, abstractmethod

class DataUpdateStrategy(ABC):

    @abstractmethod
    def update_data(self, file_path):
        pass

class NewDataUpdateStrategy(DataUpdateStrategy):

    def __init__(self):
        self.file_positions = {}

    def update_data(self, file_path):
        new_data = {}
        valid_keys = {'cs', 'trk', 'roc', 'gs', 'alt', 'lat', 'lon'}
        last_position = self.file_positions.get(file_path, 0)

        with open(file_path, 'r') as f:
            f.seek(last_position)
            reader = csv.reader(f)
            for row in reader:
                timestamp, icao, key, value = row
                timestamp = str(timestamp)
                if key not in valid_keys:
                    continue
                if icao not in new_data:
                    new_data[icao] = {}
                if timestamp not in new_data[icao]:
                    new_data[icao][timestamp] = {}
                new_data[icao][timestamp][key] = value
            self.file_positions[file_path] = f.tell()

        return new_data



class AllDataUpdateStrategy(DataUpdateStrategy):

    def update_data(self, file_path):
        data = {}
        valid_keys = {'cs', 'trk', 'roc', 'gs', 'alt', 'lat', 'lon'}
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                timestamp, icao, key, value = row
                timestamp = str(timestamp)
                if key not in valid_keys:
                    continue
                if icao not in data:
                    data[icao] = {}
                if timestamp not in data[icao]:
                    data[icao][timestamp] = {}
                data[icao][timestamp][key] = value
        return data

class Watcher(FileSystemEventHandler):

    def __init__(self, dir_path, update_strategy=None, process_at_start=True):
        self.dir_path = dir_path
        self.update_strategy = update_strategy if update_strategy is not None else NewDataUpdateStrategy()
        self.subscribers = []
        self.observer = Observer()
        self.observer.schedule(self, path=dir_path, recursive=False)
        self.observer.start()
        
        if process_at_start:
            self.process_existing_files()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            data = self.update_data(event.src_path)
            self.notify(data)

    def process_existing_files(self):
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.csv'):
                data = self.update_data(os.path.join(self.dir_path, filename))
                self.notify(data)

    def update_data(self, file_path):
        return self.update_strategy.update_data(file_path)

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, data):
        for callback in self.subscribers:
            callback(data)
if __name__ == "__main__":
    print("Watcher is not intended to be run directly. Please use it as a module. See demo programs for examples.")