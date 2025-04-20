import subprocess
from watchfiles import watch
import psutil
import time

WATCH_PATH = r"C:\projects\fast-agent-fz"
SCRIPT_PATH = r"C:\projects\fast-agent-fz\gradio_app.py"
TARGET_PORT = 7680

def should_restart(file_path: str) -> bool:
    # Define file extensions to watch
    watch_extensions = ('.py', '.html', '.css', '.js')
    # Define directories to ignore
    ignore_dirs = ['.venv', '__pycache__']
    # Check if file has the desired extension and is not in ignored directories
    return file_path.endswith(watch_extensions) and not any(ignored in file_path for ignored in ignore_dirs)

def run_app():
    return subprocess.Popen(["python", SCRIPT_PATH])

def kill_port_user(port):
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    print(f"⚠️ Killing PID {proc.pid} ({proc.name()}) using port {port}")
                    proc.kill()
                    killed = True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    if not killed:
        print(f"✅ No process found using port {port}")

if __name__ == "__main__":
    # Kill any leftover process using port BEFORE running app for the first time
    kill_port_user(TARGET_PORT)

    process = run_app()
    print(f"👀 Watching {WATCH_PATH} for changes...")

    try:
        for changes in watch(WATCH_PATH, recursive=True):
            if any(should_restart(str(change[1])) for change in changes):
                print("🔄 Detected change, restarting app...")

                process.terminate()
                process.wait()

                # Double check and kill port user again just in case
                kill_port_user(TARGET_PORT)

                time.sleep(1)
                process = run_app()
    except KeyboardInterrupt:
        print("🛑 Stopping watcher...")
        process.terminate()
        process.wait()

