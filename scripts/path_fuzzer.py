import requests
import random
import time

TARGET = "http://localhost:8080"

PATHS = [
    "/admin",
    "/wp-login.php",
    "/.env",
    "/config.php",
    "/api/unknown",
]

USER_AGENTS = [
    "Mozilla/5.0",
    "curl/7.88.1",
    "python-requests/2.31.0",
    "Scanner-Test-Agent",
]

def simulate():
    for _ in range(50):
        path = random.choice(PATHS)
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }

        try:
            requests.get(TARGET + path, headers=headers, timeout=1)
        except Exception:
            pass

        time.sleep(0.1)

if __name__ == "__main__":
    simulate()
