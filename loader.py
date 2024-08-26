import requests


def load_page(url):
    headers = {
        # 'accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    r = requests.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        return r.content
