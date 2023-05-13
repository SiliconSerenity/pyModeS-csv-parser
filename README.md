# pyModeS-csv-parser
Tools to improve the usefulness of pyModeS CSV output without modifying pyModeS itself


# CSV Watcher for pyModeS

## Overview
This Python application, referred to as CSV Watcher, is a standalone utility created to monitor changes in CSV files within a specified directory. It is designed to work with pyModeS or any CSV files that follow the expected format. 

The expected CSV file format consists of four columns: timestamp, icao, key, and value. The keys that are handled include 'cs' for callsign, 'trk', 'roc', 'gs', 'alt' for altitude, 'lat' for latitude, 'lon' for longitude.

Please note that this project does not extend or modify the pyModeS project in any way. It is a separate utility that merely uses the output produced by pyModeS or any other system that generates CSV files in the same format.

## Requirements

To use `watcher.py` and `watcher_demo.py`, you will need:

1. **Python 3:** This project is written in Python 3, and likely won't work with Python 2 due to differences in syntax and libraries. Make sure you're using Python 3 before you start.

2. **Watchdog Python Package:** The Watchdog package is used for monitoring the directory containing the CSV data files. You can install it via pip. Depending on your environment, you may need to use `pip3` instead of `pip`. This is because in some systems, `pip` is still linked to Python 2's package manager, while `pip3` is linked to Python 3's package manager. If you're in such an environment, `pip3` is the right command to use. Install with either command as shown below:

    ```bash
    pip install watchdog
    # or
    pip3 install watchdog
    ```

3. **CSV Data Files:** The application is designed to work with CSV data files in the format output by the pyModeS library. These files should have four fields in the following order: timestamp, icao, key, and value. The files should NOT have a data header row labeling these fields (i.e., the first row should be data).

## Setup

### watcher.py and watcher_demo.py
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

### watcher_demo_http.py

In order for `watcher_demo_http.py` to be useful, a corresponding server needs to be listening on the port and url it is attempting to send data to. See `web_listener_demo.py` for an example of this.

To use `watcher_demo_http.py`, you will need to ensure you have the necessary Python packages installed. These packages are:

- **requests:** This package is used for sending HTTP requests.
- **argparse:** This package is used for parsing command line arguments.

You can install these packages using pip or pip3, depending on your Python setup. Open a terminal and type the following command to install these packages:

```shell
pip install requests argparse
```

Or, if you are using Python 3 and pip3 is your package manager, type:

```shell
pip3 install requests argparse
```

Once these packages are installed, you can run `watcher_demo_http.py` as described in the Usage section.

### web_listener.py

To use `web_listener.py`, you will need to ensure you have the necessary Python packages installed. These packages are:

- **flask:** This package is used for setting up the web server.

You can install this package using pip or pip3, depending on your Python setup. Open a terminal and type the following command to install the package:

```shell
pip install flask
```

Or, if you are using Python 3 and pip3 is your package manager, type:

```shell
pip3 install flask
```
Once the flask package is installed, you can use `web_listener.py` as a module in your Python programs.


### web_listener_demo.py

To use `web_listener_demo.py`, you will need to install the `Flask` module, which is used for creating the web server. You can install it via `pip` or `pip3`, depending on your Python setup. Open a terminal and type the following command to install `Flask`:

```shell
pip install flask
```

Once `Flask` is installed, you can run the `web_listener_demo.py` script as described in the Usage section.

Please note that `web_listener_demo.py` is a demo program that demonstrates the usage of `WebListener`. It is not intended to be run directly. You can use it as a reference to implement your own handler functions and customize the behavior of the listener.

Remember to replace the handler function `data_received_handler` with your own code that processes the received data.

To run the example script, navigate to the directory containing `web_listener_demo.py` and use the following command:

```shell
python3 web_listener_demo.py
```

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
python watcher_demo_http.py --url <destination_url> --port <destination_port> --watchlocation <directory_to_watch>
```

Replace `<destination_url>`, `<destination_port>`, and `<directory_to_watch>` with your actual destination URL, port number, and the path to the directory you want to monitor. The port number will default to `80` if not specified, but `--url` and `--watchlocation` are mandatory.

# Links
pyModeS: https://github.com/junzis/pyModeS


