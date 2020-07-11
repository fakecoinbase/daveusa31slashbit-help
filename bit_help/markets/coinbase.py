import random_data

from coinbase.wallet.client import Client




class Coinbase(Client):
	random_api_key = random_data.etc.password(length=5)
	random_api_secret = random_data.etc.password(length=5)


	def __init__(self, api_key: str=random_api_key, api_secret: str=random_api_secret):
		super().__init__(api_key, api_secret) # Наследуем класс coinbase
		self.client = Client(api_key, api_secret)

	def price(self, currency="USD"):
		currency_pair = "BTC-{}".format(currency.upper()) 
		price = self.client.get_buy_price(currency_pair=currency_pair)["amount"]
		return float(price)