import bit_help


coindesk = bit_help.markets.Coindesk()

print(coindesk.price(currency="RUB"))

# # print(helper.Coindesk().historical_data())
print(coindesk.supported_currencies())

