import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            print("Detected file change. Reloading server...")
            os.system('app.py')

if __name__ == "__main__":
    path = '.'
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Watching for file changes...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
