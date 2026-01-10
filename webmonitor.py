
import requests
import time
import winsound # For the alarm

# 1. List of Websites to Monitor
SITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://this-site-does-not-exist.com" # Fake site to test error
]

CHECK_INTERVAL = 5 # Check every 5 seconds
print("Website Monitor Started...")
def check_sites():
    for site in SITES:
        try:
            # 2. Send a "GET" request (Like opening a browser)
            response = requests.get(site, timeout=3)

            # 3. Check Status Code (200 = OK)
            if response.status_code == 200:
                print(f"UP: {site}")
            else:
                print(f"DOWN ({response.status_code}): {site}")
                winsound.Beep(1000, 500) # Beep if status is not 200

        except requests.exceptions.ConnectionError:

            print(f"FAILED: {site} (Connection Error)")
            winsound.Beep(2000, 1000) # Long Beep for crash
while True:
    check_sites()
    print("-" * 30)
    time.sleep(CHECK_INTERVAL)

