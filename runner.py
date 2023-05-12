from watcher import Watcher
import time

def data_changed_handler(data):
    print(data)

wd = Watcher('./data')
wd.subscribe(data_changed_handler)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
