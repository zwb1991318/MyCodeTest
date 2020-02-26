import requests

if __name__ == "__main__":
    response = requests.get("http://www.baidu.com")
    print(response.status_code)
    response.encoding = "UTF-8"
    print(response.text)
    print(type(response))
    print(response.headers)
    requests.request