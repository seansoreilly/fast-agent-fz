import subprocess
import time
from watchfiles import watch

WATCH_PATH = r"C:\projects\fast-agent-fz"
SCRIPT_PATH = r"C:\projects\fast-agent-fz\gradio_app.py"

def should_restart(file_path: str) -> bool:
    # Define file extensions to watch
    watch_extensions = ('.py', '.html', '.css', '.js')
    # Define directories to ignore
    ignore_dirs = ['.venv', '__pycache__']
    # Check if file has the desired extension and is not in ignored directories
    return file_path.endswith(watch_extensions) and not any(ignored in file_path for ignored in ignore_dirs)

def run_app():
    return subprocess.Popen(["python", SCRIPT_PATH])

if __name__ == "__main__":
    process = run_app()
    print(f"👀 Watching {WATCH_PATH} for changes...")

    try:
        for changes in watch(WATCH_PATH, recursive=True):
            if any(should_restart(str(change[1])) for change in changes):
                print("🔄 Detected change, restarting app...")
                process.terminate()
                process.wait()
                process = run_app()
    except KeyboardInterrupt:
        print("🛑 Stopping watcher...")
        process.terminate()
        process.wait()
