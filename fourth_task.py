import requests


def get_public_ip():
    url = "https://ifconfig.me/ip"
    response = requests.get(url)
    return response.text


print(get_public_ip())