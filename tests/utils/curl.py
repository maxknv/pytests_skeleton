import requests


class Curl:
    @staticmethod
    def request_post(url, json=None):
        try:
            r = requests.post(url, json=json)
        except requests.exceptions.ConnectionError:
            return None, {}
        return r.status_code, r.json() if r.status_code == 200 else {}

    @staticmethod
    def request_get(url):
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            return None, {}
        return r.status_code, r.json()
