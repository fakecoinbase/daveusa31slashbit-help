import random_data
import blockcypher

from coinbase.wallet.client import Client


class Coinbase(Client):
    random_api_key = random_data.etc.password(length=5)
    random_api_secret = random_data.etc.password(length=5)


    def __init__(self, api_key: str=random_api_key, api_secret: str=random_api_secret):
        super().__init__(api_key, api_secret) # Наследуем класс coinbase
        self.client = Client(api_key, api_secret)
        self.account_id = self.client.get_primary_account()["id"]

    def price(self, currency="USD"):
        currency_pair = "BTC-{}".format(currency.upper()) 
        price = self.client.get_buy_price(currency_pair=currency_pair)["amount"]
        return float(price)

    def address_balance(self, address_id, confirmations=1):
        balance = 0

        data = self.client.get_address_transactions(self.account_id, address_id)
        transactions = data["data"]


        if 0 < len(transactions):
            for transaction in transactions:
                hash = transaction["network"]["hash"]
                transaction_sum = float(transaction["amount"]["amount"])

                if 3 <= confirmations:
                    if "confirmed" == transaction["network"]["status"]:
                        balance += transaction_sum

                elif 0 < confirmations and 3 > confirmations:
                    transaction_info = blockcypher.get_transaction_details(hash)
                    transaction_confirmations = transaction_info["confirmations"]

                    if confirmations <= transaction_confirmations:
                        balance += transaction_sum

                elif 0 == confirmations:
                    balance += transaction_sum

        return balance