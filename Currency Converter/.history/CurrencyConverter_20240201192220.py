import requests

from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

rates = requests.get

response = requests.get(f"https://api.frankfurter.app/latest?rates
                        ?amount={amount}&from={from_currency}&to={to_currency}")
