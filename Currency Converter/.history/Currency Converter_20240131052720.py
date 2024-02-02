import requests

from_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(f"https://v6.exchangerate-api.com/v6/43fed482850619003c1e4129/latest/USD()")

