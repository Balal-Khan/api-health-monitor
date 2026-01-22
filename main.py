import argparse
from monitor.checker import check_api_health

def main():
    parser = argparse.ArgumentParser(description = "API Health Monitor")
    parser.add_argument("url", help = "API endpoint to check")
    parser.add_argument("--retries", type=int, default = 3, help = "Number of retry attempts")
    parser.add_argument("--timeout", type=int, default = 5, help = "Request timeout in seconds")
    
    args = parser.parse_args()
    
    healthy = check_api_health(
        args.url,
        retries = args.retries,
        timeout = args.timeout
    )
    
    if healthy:
        print("API is HEALTHY")
    else:
        print("API is NOT HEALTHY")


if __name__ == "__main__":
    main()