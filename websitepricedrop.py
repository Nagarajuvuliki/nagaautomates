import requests
from bs4 import BeautifulSoup
import smtplib
import time# 1. Configuration
URL = 'https://example.com'  # Replace with real URL
TARGET_PRICE = 124900.00
MY_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password" # Generated from Google Account Security
def check_price():
    # 2. Get the HTML
    headers = {"User-Agent": "Mozilla/5.0"} # Pretend to be a browser
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # 3. Find the Price (Inspect Element on the site to find the ID/Class)
    # Example: <span id="price_inside_buybox">1,499.00</span>
    price_text = soup.find(id="price_inside_buybox").get_text()
    # Clean the data (remove currency symbols and commas)
    price = float(price_text.replace('', '').replace(',', '').strip())
    print(f"Current Price: {price}")
    # 4. Compare and Alert
    if price < TARGET_PRICE:
        send_email(price)
    else:
        print("Price is still too high. Checking again later...")
def send_email(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_EMAIL, APP_PASSWORD)
    subject = "PRICE DROP ALERT!"
    body = f"The product is now {price}! Buy it here: {URL}"
    msg = f"Subject: {subject}{body}"
    server.sendmail(MY_EMAIL, MY_EMAIL, msg)
    print("Email Alert Sent!")
    server.quit()

# Run the check
#check_price() only if you want to put in task schedular or linux on cron
while True:
    check_price()
    time.sleep(86400) # Check once every day (86400 seconds)

