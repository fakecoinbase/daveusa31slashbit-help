import bit_help
from bit_help import markets

coinbase = markets.Coinbase("oM7Lz4b7Q7MnJ8tY", "CTc1OKw4bq9r75eH4PsnBbEtSkDr5woP")


address_id = "6fc34503-9aa3-542e-882a-bf70a621faa9"


balance = coinbase.address_balance(address_id)
print(bit_help.format_sum(balance))

