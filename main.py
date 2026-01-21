from monitor.checker import check_api_health


def main():
    url = "https://httpbin.org/status/200"
    result = check_api_health(url)
    
    print("\n=== API HEALTH CHECK ===")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()