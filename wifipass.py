import subprocess

# 1. Get data from the 'netsh' command
# We run: netsh wlan show profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace")
# 2. Split the data to find profile names
profiles = [i.split(":")[1][1:-1] for i in data.split('\n') if "All User Profile" in i]
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-" * 50)
# 3. Loop through each WiFi profile to get the password
for i in profiles:
    try:
        # Run: netsh wlan show profile "Name" key=clear
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace")

        # 4. Extract the password line
        results = [b.split(":")[1][1:-1] for b in results.split('\n') if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, "Open Network (No Password)"))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(i, "Error"))
input("\nPress Enter to Exit...")