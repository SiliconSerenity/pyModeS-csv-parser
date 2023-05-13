# pyModeS-csv-parser
Tools to improve the usefulness of pyModeS CSV output without modifying pyModeS itself


# CSV Watcher for pyModeS

## Overview
This Python application, referred to as CSV Watcher, is a standalone utility created to monitor changes in CSV files within a specified directory. It is designed to work with pyModeS or any CSV files that follow the expected format. 

The expected CSV file format consists of four columns: timestamp, icao, key, and value. The keys that are handled include 'cs' for callsign, 'trk', 'roc', 'gs', 'alt' for altitude, 'lat' for latitude, 'lon' for longitude.

Please note that this project does not extend or modify the pyModeS project in any way. It is a separate utility that merely uses the output produced by pyModeS or any other system that generates CSV files in the same format.

## Requirements

To use `watcher.py` and `runner.py`, you will need:

1. **Python 3:** This project is written in Python 3, and likely won't work with Python 2 due to differences in syntax and libraries. Make sure you're using Python 3 before you start.

2. **Watchdog Python Package:** The Watchdog package is used for monitoring the directory containing the CSV data files. You can install it via pip. Depending on your environment, you may need to use `pip3` instead of `pip`. This is because in some systems, `pip` is still linked to Python 2's package manager, while `pip3` is linked to Python 3's package manager. If you're in such an environment, `pip3` is the right command to use. Install with either command as shown below:

    ```bash
    pip install watchdog
    # or
    pip3 install watchdog
    ```

3. **CSV Data Files:** The application is designed to work with CSV data files in the format output by the pyModeS library. These files should have four fields in the following order: timestamp, icao, key, and value. The files should NOT have a data header row labeling these fields (i.e., the first row should be data).

To use `remote_sender.py`, you will additionally need:

4. **python-dotenv:** A dependency used for reading environment variables stored in a .env file.
```bash
pip install python-dotenv
# or
pip3 install python-dotenv
```

## Setup

### watcher.py and runner.py
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

### remote_sender.py

In order to use `remote_sender.py`, you need to setup the environment variables `REMOTE_SENDER_DESTINATION_URL` and `REMOTE_SENDER_DESTINATION_PORT`. These variables are used by the script to determine the server to which it needs to send the data. To do this, create a `.env` file in the same directory as `remote_sender.py` and set the variables in the following format:

```bash
REMOTE_SENDER_DESTINATION_URL=<your_destination_url>
REMOTE_SENDER_DESTINATION_PORT=<your_destination_port>
```

Replace `<your_destination_url>` and `<your_destination_port>` with your actual destination URL and port. 

If `REMOTE_SENDER_DESTINATION_PORT` is not specified in the `.env` file, the script will use a default port of 8000.

Please note that if `REMOTE_SENDER_DESTINATION_URL` is not specified in the `.env` file, the script will exit with a warning since this is a required parameter.

After setting up the `.env` file, you can run `remote_sender.py` as described in the Usage section.




## Usage

### watcher.py
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

Refer to `runner.py` for a working example. 

### remote_sender.py

The `remote_sender.py` script is used to send data to a remote destination. Fundamentally, it has the same processing loop as `runner.py`: Wait for data to change, and when it does, do something. 

Unlike `runner.py`, which simply prints the data to the console as a trivial example, `remote_sender.py` is an example of a usage of `watcher.py` that actually does something useful with the data, namely sending it somewhere else! It reads the destination URL and port number from the environment variables. 

Before running the script, you need to set these environment variables in a `.env` file in your project's root directory:

```bash
REMOTE_SENDER_DESTINATION_URL=<your_destination_url>
REMOTE_SENDER_DESTINATION_PORT=<your_destination_port>
```

Replace `<your_destination_url>` and `<your_destination_port>` with your actual destination URL and port number. The port number will default to `80` if not specified, but you will receive an error if you do not specify a URL.

To run `remote_sender.py`, navigate to the directory containing the script and use the following command:

```bash
python3 remote_sender.py [dir_path]
```

Where `[dir_path]` is the path to the directory you want to monitor.


# Links
pyModeS: https://github.com/junzis/pyModeS