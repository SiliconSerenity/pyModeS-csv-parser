import sys
import time
from pymodes_csv_parser.watcher import Watcher
from pymodes_csv_parser.loader import Loader

def data_changed_handler(data):
    print(data)

if len(sys.argv) < 2:
    print("Usage: python3 runner.py [dir_path]")
    sys.exit(1)

dir_path = sys.argv[1]
wd = Watcher(dir_path)
ld = Loader(dir_path)

wd.subscribe(data_changed_handler)

print("Get initial data:")
print(ld.getData())



print("Watching directory: {}".format(dir_path))
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
