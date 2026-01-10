import requests
import time
from datetime import datetime

# 1. API Endpoint (The URL that gives us data)
# We are asking for Bitcoin price in USD
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

print("Starting Live Crypto Tracker...\n")
def get_bitcoin_price():
    try:
        # 2. Fetch Data
        response = requests.get(URL)

        # 3. Check if request was successful
        if response.status_code == 200:
            # 4. Parse JSON (Convert text to Python Dictionary)
            data = response.json()

            # Extract the specific price
            price = data['bitcoin']['usd']

            # Get current time
            now = datetime.now().strftime("%H:%M:%S")

            print(f"[{now}] Bitcoin Price: ${price}")
        else:
            print("Failed to fetch data.")
    except Exception as e:
        print(f"Error :{e}")

# 5. Run forever (Loop)
while True:
    get_bitcoin_price()
    time.sleep(10) # Update every 10 seconds
    
