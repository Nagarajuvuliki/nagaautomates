import paramiko
import time
from datetime import datetime
# 1. SERVER DETAILS
HOST = "192.168.1.1"  # Router IP
USER = "mainrouter"
PASS = "password"
# 2. Get Current Date for Filename (e.g., backup_2025-01-03.txt)
date_now = datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = f"backup_{date_now}.txt"
print(f"Connecting to {HOST}...")
try:
    # 3. Create SSH Client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, username=USER, password=PASS)
    # 4. Open Interactive Shell (Crucial for Network Gear!)
    shell = client.invoke_shell()
    # Send commands (Wait 1 sec between commands for router to process)
    shell.send("terminal length 0") # Disable pagination (Important!)
    time.sleep(1)
    shell.send("show running-config")
    time.sleep(3) # Wait for big config to load
    # 5. Receive Output
    output = shell.recv(65535).decode("utf-8")
    # 6. Save to File
    with open(filename, "w") as f:
        f.write(output)
    print(f'Backup Successful! Saved as :{filename}')
    client.close()
except Exception as e:
    print(f'error : {e}')