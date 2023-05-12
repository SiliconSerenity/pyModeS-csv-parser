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
Coming Soon
