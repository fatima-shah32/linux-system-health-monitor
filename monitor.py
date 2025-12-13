import psutil
from datetime import datetime

LOG_FILE = "logs/system_health.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def system_health():
    log("=" * 50)
    log(f"System Health Check - {datetime.now()}")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())

    log(f"CPU Usage: {cpu}%")
    log(f"Memory Usage: {memory}%")
    log(f"Disk Usage: {disk}%")
    log(f"System Uptime: {uptime}")

if __name__ == "__main__":
    system_health()

