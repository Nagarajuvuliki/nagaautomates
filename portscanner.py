
import socket
import datetime
# 1. Define the Target (Use your own Router IP or 'scanme.nmap.org')
TARGET_IP = "192.168.1.1" 
START_PORT = 20
END_PORT = 100
print(f"Starting Scan on {TARGET_IP}...")
print(f"Time: {datetime.datetime.now()}")
try:
    # 2. Loop through the ports
    for port in range(START_PORT, END_PORT + 1):
        # Create a socket object (IPV4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout to 0.5 seconds (Make it fast!)
        socket.setdefaulttimeout(0.5)
        # 3. Try to connect
        # result returns 0 if connection is successful (Open Port)
        result = s.connect_ex((TARGET_IP, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("Scan Stopped by User.")
except socket.error:
    print("Could not connect to server.")
print("Scan Completed")