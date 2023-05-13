# pyModeS-csv-parser
Tools to improve the usefulness of pyModeS CSV output without modifying pyModeS itself


# CSV Watcher for pyModeS

## Overview
The core of this repository is the CSV Watcher, or just Watcher. It is a class designed to be reusable in a variety of python programs to easily automate processing of data collected and output to CSV format by the pyModeS library. In addition to the Watcher, several useful examples of functionality are provided, but keep in mind that the Watcher is the first link in the chain for all of their functionality.

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

### watcher.py
This package provides a `Watcher` class that monitors a directory for changes in CSV files and updates an internal data structure accordingly. It also includes a simple usage example in `watcher_demo.py` that demonstrates how to use the `Watcher` class and prints updated data to the console whenever a CSV file is modified.

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

To run the example script, navigate to the directory containing `watcher_demo.py` and use the following command:

```bash
python3 watcher_demo.py [dir_path]
```

Where `[dir_path]` is the path to the directory you want to monitor.

Refer to `watcher_demo.py` for a working example. 


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