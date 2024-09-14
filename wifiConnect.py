import network
import urequests as requests
from time import sleep
import machine

# Replace with your actual Firebase Realtime Database URL and token
database_url = "https://bu-ec463-default-rtdb.firebaseio.com/test.json?auth=W8n0ypLxs9OC3dAZAugyQKekuLheuYnJzR0NrVme"

# Example data to send
data = {"message": "Hello from MicroPython!"}

ssid = "BU Guest (unencrypted)"

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected:', wlan.ifconfig())

try:
    connect()
except KeyboardInterrupt:
    machine.reset()

# Send a POST request to the database
response = requests.post(database_url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Data posted successfully")
else:
    print(f"Failed to post data. Status code: {response.status_code}")
