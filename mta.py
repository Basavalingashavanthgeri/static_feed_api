import requests


class MtaClass:

    def __init__(self, staticUrl):
        self.staticUrl = staticUrl

    def mta(self):
        response = requests.get(self.staticUrl)
        return response.content
