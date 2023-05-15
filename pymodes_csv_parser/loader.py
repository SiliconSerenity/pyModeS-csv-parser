import os
from pymodes_csv_parser.update_strategies import AllDataUpdateStrategy
   
class Loader:
    def __init__(self, dir_path, scan_on_startup=True, update_strategy=None):
        self.dir_path = dir_path
        self.update_strategy = update_strategy if update_strategy is not None else AllDataUpdateStrategy()
        self.data = {} #initialize data
        if scan_on_startup:
            self.scan() #populate data

    def scan(self):
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.csv'):
                new_data = self.update_data(os.path.join(self.dir_path, filename))
                self.data.update(new_data) #combine data from this file with data from other files
        return self.data

    def getData(self):
        return self.data

    def update_data(self, file_path):
        return self.update_strategy.update_data(file_path)