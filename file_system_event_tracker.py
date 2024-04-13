import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/rkdha/Downloads"
to_dir = "C:/Users/rkdha/Desktop/Downloaded_Files"

#Event Handler Class

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Hey {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Hey {event.src_path} has been moved")

# Initialize Event Handler Class
    event_handler = FileEventHandler()


# Initialize Observer
    observer = Observer()

# Schedule the Observer
    observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
    observer.start()