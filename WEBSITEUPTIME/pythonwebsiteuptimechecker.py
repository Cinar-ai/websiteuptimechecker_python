import requests
import time
from datetime import datetime

sites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsite12345.com"
]

CHECK_INTERVAL = 30
LOG_FILE = "UptimeLog.txt"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

print("Uptime checker started./n")

while True:
    for site in sites:
        try:
            r = requests.get(site, timeout=5)
            status = f"{site}UP {r.status_code}"

            print("🆗", status)
        except requests.RequestException as e:
            status = f"{site}DOWN ({e})"
            print("❌", status)
        log(f"{datetime.now()}: {status}")
    print()
    time.sleep(CHECK_INTERVAL)