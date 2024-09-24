import requests

print("=============================")
print("Exchange Rate App By BioZFrog")
print("=============================\n")
API_KEY = 'API-KEY'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

# Function to get the exchange rates between two currencies
def get_exchange_rates(base_currency, second_currency):
    response = requests.get(BASE_URL + base_currency)  
    if response.status_code == 200:  
        data = response.json()  
        return data['conversion_rates'][second_currency]  
    else:
        print("Error:", response.status_code)  
        return None

# Asking for for the base and target currencies
base_currency = input("Enter the Base Currency: ")
target_currency = input(f"Enter the Target Currency: ")
conversion_amount  = input(f"How much {base_currency} do you want to convert to {target_currency}? ")
conversion_amount  = int(conversion_amount) # Converting input into an integer

# Using the function to get exchange rate between the base and the target currencies
rate = get_exchange_rates(base_currency, target_currency)
rate = float(rate) # Converting the exchange rate into a float
rate = rate * conversion_amount  # Multiplying the exchange rate by the input conversion amount

if rate:
    print(f"\n{conversion_amount} {base_currency} is approximately {rate} {target_currency}")
