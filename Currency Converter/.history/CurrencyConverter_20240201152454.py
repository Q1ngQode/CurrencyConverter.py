import requests

from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

rates = requests.get

response = requests.get(f"https://data.fixer.io/api/access_key=f5b6b69539cb465b8ec9bcd7226c9350/latest?rates?amount={amount}&from={from_currency}&to={to_currency}")
print (f"{amount} {from_currency} is {response.json() [rates'][to_currency]} {to_currency}")