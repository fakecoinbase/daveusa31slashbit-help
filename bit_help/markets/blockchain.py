import requests


from .. import exceptions


class Blockchain:
    __URL = "https://blockchain.info/"
    """
    Доступные методы:
        address_info
    """

    def __init__(self):
        pass

    def address_info(self, address):
        path = "address/{}".format(address)
        return self.__requests(path)



    def __requests(self, path):
        url = self.__URL + path

        params = {
            "format": "json",
        }
        return requests.get(url, params=params).json()



