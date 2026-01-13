import requests
import time
# 1. TELEGRAM CONFIGURATION
# Search for 'BotFather' in Telegram to get a Token
BOT_TOKEN = "Your bot token"
# Search for 'userinfobot' in Telegram to get your ID
CHAT_ID = "Your chat ID"
def send_telegram_alert(message):
    try:
        # 2. The Magic URL
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        # 3. Data to send
        payload = {"chat_id": CHAT_ID,"text": message}
        # 4. Send the Request
        requests.post(url, data=payload)
        print(f"Alert Sent: {message}")
    except Exception as e:
        print(f"Error sending alert: {e}")

# --- DEMO: Let's pretend Bitcoin just crashed ---
print("Monitoring Critical Events...")
# Simulate a check (You can paste your Crypto or Website code here)
current_price = 45000
threshold = 50000
if current_price < threshold:
    msg = f"URGENT: Bitcoin dropped to ${current_price}! Buy now!"
    send_telegram_alert(msg)
    