
import psutil
import time
import winsound  # Only works on Windows


# SETTINGS
CPU_THRESHOLD = 80  # Alert if CPU is above 80%
RAM_THRESHOLD = 80  # Alert if RAM is above 80%
CHECK_INTERVAL = 2  # Check every 2 seconds

print(" System Monitor Started... Press Ctrl+C to Stop.")

try:
    while True:
        # Get System Stats
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        # Print the status
        print(f"CPU: {cpu_usage}% | RAM: {ram_usage}%")

        # CHECK FOR HIGH CPU
        if cpu_usage > CPU_THRESHOLD:
            print("ALERT: High CPU Usage!")
            # Frequency 1000Hz, Duration 500ms
            winsound.Beep(1000, 500) 

            # CHECK FOR HIGH RAM
        if ram_usage > RAM_THRESHOLD:
            print("ALERT: High RAM Usage!")
            winsound.Beep(2000, 500)

            time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("Monitor Stopped.")
