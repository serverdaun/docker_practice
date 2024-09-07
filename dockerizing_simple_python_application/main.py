import requests


def get_quote(url):
    response = requests.get(url)
    print(response.json()['quote'])

get_quote('https://api.kanye.rest')
