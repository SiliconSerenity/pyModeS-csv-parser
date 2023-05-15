# pyModeS-csv-parser
Tools to improve the usefulness of pyModeS CSV output without modifying pyModeS itself


# CSV Watcher for pyModeS

## Overview
The core of this repository consists of two main components: the CSV Loader and the CSV Watcher. The CSV Loader is responsible for loading data from existing CSV files, while the CSV Watcher is designed to obtain new data as it is appended to CSV files, or as new CSV files are created. These classes are designed to be reusable in a variety of python programs to easily automate processing of data collected and output to CSV format by the pyModeS library. In addition to the Loader and Watcher, several useful examples of functionality are provided. However, it's important to note that the Loader and Watcher serve as the foundational elements for all downstream functionality.

See the Requirements section for details about the CSV format.

Please note that this project does not extend or modify the pyModeS project in any way. This project is simply a set of separate utilities that merely use the output produced by pyModeS or any other system that generates CSV files in the same format.

The overall goal of this project is to make it easy to perform additional automated processing on the CSV output of pyModeS, without modifying pyModeS itself.

## Requirements

To use `watcher.py` and `watcher_demo.py`, you will need:

1. **Python 3:** This project is written in Python 3, and likely won't work with Python 2 due to differences in syntax and libraries. Make sure you're using Python 3 before you start.

2. **Python Dependencies:** This project has several Python dependencies, which are listed in the requirements.txt file. You can install them using `pip`, the Python package installer. Depending on your environment, you may need to use `pip3` instead of `pip`. This is because, in some systems, `pip` is still linked to Python 2's package manager, while `pip3` is linked to Python 3's package manager. If you're in such an environment, `pip3` is the right command to use. When in doubt, try `pip3`.

    To install the dependencies, navigate to the project directory and run the following command:

    For `pip3`:
    ```bash
        pip3 install -r requirements.txt
    ```
    For `pip`:
    ```bash
        pip install -r requirements.txt
    ```
3. **CSV Files:** The application is designed to work with CSV data files in the format output by the pyModeS as of May 2023. The expected CSV file format consists of four columns: timestamp, icao, key, and value. The keys that are handled include `'cs'` for callsign, `'trk'`, `'roc'`, `'gs'`, `'alt'` for altitude, `'lat'` for latitude, and `'lon'` for longitude. Any other keys are ignored.

    The files should NOT have a data header row labeling these fields (i.e., the first row should be data).

## Usage

### watcher.py and loader.py

This package provides two classes: `Watcher` and `Loader`. The `Watcher` class is responsible for monitoring a directory for changes in CSV files, while the `Loader` class is responsible for loading data from existing CSV files.

#### Watcher

The `Watcher` class includes a simple usage example in `watcher_demo.py` that demonstrates how to use the `Watcher` class and prints updated data to the console whenever a CSV file is modified.

Here's an example of how to use the `Watcher`:

```python
from pymodes_csv_parser.watcher import Watcher

# Define a handler function
def data_changed_handler(data):
    # Write your code that does stuff with the data here!
    print(data) # for example, simply print the data to the console

# Create a new Watcher
wd = Watcher('./data')
# Subscribe the handler
wd.subscribe(data_changed_handler)
```

By default, the `Watcher` does not maintain an internal data structure as it only triggers the provided handler function whenever a CSV file is modified.

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

To run the example script, navigate to the directory containing `watcher_demo.py` and use the following command:

```bash
python3 watcher_demo.py [dir_path]
```

Where `[dir_path]` is the path to the directory you want to monitor.

Refer to `watcher_demo.py` for a working example.

#### Loader

The `Loader` class is responsible for loading data from existing CSV files and maintaining an internal data structure. You can use it as follows:

```python
from pymodes_csv_parser.loader import Loader

# Create a new Loader
ld = Loader('./data')
# Load the data from CSV files
data = ld.load_data()

# Process the loaded data
# Your code goes here
```

To customize the behavior of the `Loader`, you can pass additional arguments to the `Loader` constructor:

- `scan_on_startup=False`: The `Loader` will not process files at startup, and the scan function must be invoked. This might be useful if you want to wait to do an initial scan for some reason.


You can also force a re-scan at any time, regardless of whether a scan was performed on startup, with the `scan` method:
```python
from pymodes_csv_parser.loader import Loader

ld = Loader('./data', scan_on_startup=False)
data = ld.getData() # returns {}
ld.scan()
data = ld.getData() # returns populated data

```


Replace `'./data'` with the path to the directory containing the CSV files you want to load.

Refer to `watcher_demo.py` for a working example, as it shows both the loader and the watcher in action.



### watcher_demo_http.py
The watcher_demo_http.py script is used to send data to a remote destination. Fundamentally, it has the same processing loop as watcher_demo.py: Wait for data to change, and when it does, do something.

Unlike watcher_demo.py, which simply prints the data to the console as a trivial example, watcher_demo_http.py is an example usage of watcher.py that actually does something useful with the data, namely sending it somewhere else! It accepts the destination URL and port number as command line arguments.

To run watcher_demo_http.py, navigate to the directory containing the script and use the following command:

```bash
python3 watcher_demo_http.py --url <destination_url> --port <destination_port> --watchlocation <directory_to_watch>
```

Replace `<destination_url>`, `<destination_port>`, and `<directory_to_watch>` with your actual destination URL, port number, and the path to the directory you want to monitor. The port number will default to `80` if not specified, but `--url` and `--watchlocation` are mandatory.

# Links
pyModeS: https://github.com/junzis/pyModeS