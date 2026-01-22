import time
import requests


def check_api_health(url: str, retries = 3, timeout = 5) -> dict:
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout = timeout)
            return response.status_code == 200
            
        except requests.RequestException:
            if attempt == retries:
                return False
            time.sleep(1)