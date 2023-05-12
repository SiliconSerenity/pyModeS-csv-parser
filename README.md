# pyModeS-csv-parser
Tools to improve the usefulness of pyModeS CSV output without modifying pyModeS itself


# CSV Watcher for pyModeS

## Overview
This Python application, referred to as CSV Watcher, is a standalone utility created to monitor changes in CSV files within a specified directory. It is designed to work with pyModeS or any CSV files that follow the expected format. 

The expected CSV file format consists of four columns: timestamp, icao, key, and value. The keys that are handled include 'cs' for callsign, 'trk', 'roc', 'gs', 'alt' for altitude, 'lat' for latitude, 'lon' for longitude.

Please note that this project does not extend or modify the pyModeS project in any way. It is a separate utility that merely uses the output produced by pyModeS or any other system that generates CSV files in the same format.


## Setup

Before you can use CSV Watcher, you need to install the Python `watchdog` package, which is a dependency for this project.

You can install `watchdog` using pip or pip3, depending on your Python setup. Open a terminal and type the following command to install `watchdog`:

```shell
pip install watchdog
```

Or, if you are using Python 3 and pip3 is your package manager, type:

```shell
pip3 install watchdog
```

Once `watchdog` is installed, you can run CSV Watcher as described in the Usage section.


## Usage

This package provides a `Watcher` class that monitors a directory for changes in CSV files and updates an internal data structure accordingly. It also includes a simple usage example in `runner.py` that demonstrates how to use the `Watcher` class and prints updated data to the console whenever a CSV file is modified.

Here's an example on how to use the `Watcher`:

```python
from watcher import Watcher

# Define a handler function
def data_changed_handler(data):
    # Write your code that does stuff with the data here!
    print(data) #for example, simply print the data to the console

# Create a new Watcher
wd = Watcher('./data')
# Subscribe the handler
wd.subscribe(data_changed_handler)
```

By default, the `Watcher` will process all CSV files in the directory at startup. This behavior can be customized by passing a `process_at_start=False` argument to the `Watcher` constructor:

```python
# Create a new Watcher that does not process files at startup
wd = Watcher('./data', process_at_start=False)
```

Remember to replace `'./data'` with the path to the directory you want to monitor.

To keep your main script running (since the watcher runs as a child thread and would terminate if your main script closes), you should include a loop:

```python
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
```

If you use this looping code, you can stop the script at any time by pressing `Ctrl+C`.

To run the example script, navigate to the directory containing `runner.py` and use the following command:

```bash
python3 runner.py [dir_path]
```

Where `[dir_path]` is the path to the directory you want to monitor.
