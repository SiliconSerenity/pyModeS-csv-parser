from abc import ABC, abstractmethod
import csv

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