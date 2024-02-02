#fetches API to gather today's currency amounts including rates, and convert them from one world currency to another.

#Utilizes requests library
import requests

#Currency converting from
from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

#Currency converting to
to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

#Amount of currency to be converted
amount = float(input("Enter in the amount of money: "))

#rates = requests.get

#Fetches API - Frankfurter API 
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")


print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")