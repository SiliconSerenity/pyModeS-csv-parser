from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pymodes_csv_tools.DataUpdateStrategies import NewDataUpdateStrategy

class Watcher(FileSystemEventHandler):

    def __init__(self, dir_path, update_strategy=None):
        self.dir_path = dir_path
        self.update_strategy = update_strategy if update_strategy is not None else NewDataUpdateStrategy()
        self.subscribers = []
        self.observer = Observer()
        self.observer.schedule(self, path=dir_path, recursive=False)
        self.observer.start()

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.csv'):
            data = self.update_data(event.src_path)
            self.notify(data)

    def update_data(self, file_path):
        return self.update_strategy.update_data(file_path)

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, data):
        for callback in self.subscribers:
            callback(data)
