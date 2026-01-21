import time
import requests


def check_api_health(url: str, timeout: int = 5) -> dict:
    start_time = time.time()
    
    try:
        response = requests.get(url, timeout = timeout)
        response_time = time.time() - start_time
        
        return {
            "url": url,
            "status": "UP" if response.status_code == 200 else "DOWN",
            "status_code": response.status_code,
            "response_time_ms": round(response_time * 1000, 2)
        }
    
    except requests.RequestException as e:
        return {
            "url": url,
            "status": "DOWN",
            "error": str(e)
        }