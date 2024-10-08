"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import requests
import network
from time import sleep


ssid = "BU Guest (unencrypted)"


N: int = 10 # setting this to 10 flashes so it matches with the exercise requirement
sample_ms = 10.0
on_ms = 500

def encode_email_for_url(email):
    # Replace common special characters with their URL-encoded equivalents
    return email.replace("@", "-at-").replace(".", "-dot-")

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    wlan.connect(ssid)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    
    print("Connected")

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)



def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)
        


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)

def send_json(username: str,data: dict, json_filename: str) -> None:
    
    name = encode_email_for_url(username)
 
    database_url = f"https://bu-ec463-default-rtdb.firebaseio.com/{name}/{json_filename}?auth=W8n0ypLxs9OC3dAZAugyQKekuLheuYnJzR0NrVme"
    
    requests.put(database_url, json=data)

def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]
    
    #Added by Albert for exercise 3:
    if t_good:
        min_time = min(t_good)
        max_time = max(t_good)
        avg_time = sum(t_good) / len(t_good)
        
        print(f"Minimum response time: {min_time} ms")
        print(f"Maximum response time: {max_time} ms")
        print(f"Average response time: {avg_time:.2f} ms")
    else:
        min_time = max_time = avg_time = None
        print("No valid responses to calculate times")
    

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    
    score = (len(t_good) / len(t)) if len(t) > 0 else 0.0
    
    # Prepare data for JSON
    data = {
        "misses": misses,
        "min_response_time": min_time,
        "max_response_time": max_time,
        "avg_response_time": avg_time,
        "score": score,
    }

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)
    
    #get user input
    username = input("Enter your email: ")
    
    send_json(username, data, filename)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)
    
    connect()

    scorer(t)
