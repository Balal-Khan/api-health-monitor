from monitor.checker import check_api_health


def test_api_up():
    result = check_api_health("https://httpbin.org/status/200")
    assert result["status"] == "UP"
    

def test_api_down():
    result = check_api_health("https://httpbin.org/status/500")
    assert result["status"] == "DOWN"
    