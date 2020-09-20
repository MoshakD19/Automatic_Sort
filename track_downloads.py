import sys
import schedule
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

def main():
    try:
        while True:
            time.sleep(3)
            os.system('python3 sorter.py')
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "/Users/shakurduale/Downloads"
    log_handler = LoggingEventHandler()
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(log_handler, path, recursive=True)
    observer.start()
    event_handler.on_created(main())
