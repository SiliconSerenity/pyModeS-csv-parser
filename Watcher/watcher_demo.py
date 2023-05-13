import sys
import time
from watcher import Watcher

def data_changed_handler(data):
    print(data)

if len(sys.argv) < 2:
    print("Usage: python3 runner.py [dir_path]")
    sys.exit(1)

dir_path = sys.argv[1]
wd = Watcher(dir_path)
wd.subscribe(data_changed_handler)

print("Get initial data:")
print(wd.getData())



print("Watching directory: {}".format(dir_path))
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
