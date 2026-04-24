import requests
import random
import time

URL = "http://127.0.0.1:8000/detect"

while True:
    payload = {
        "login_attempts": random.randint(1, 10),
        "unusual_ip": random.choice([True, False]),
        "geo_mismatch": random.choice([True, False])
    }

    res = requests.post(URL, json=payload)
    print(res.json())

    time.sleep(2)