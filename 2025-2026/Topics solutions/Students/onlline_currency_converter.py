# onlline_currency_converter

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """
    Convert an amount from one currency to another using provided exchange rates.

    :param amount: The amount of money to convert.
    :param from_currency: The currency code of the original currency.
    :param to_currency: The currency code of the target currency.
    :param exchange_rates: A dictionary with currency codes as keys and their exchange rates as values.
    :return: The converted amount in the target currency.
    """
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency code provided.")

    # Convert the amount to a base currency (e.g., USD) first
    base_amount = amount / exchange_rates[from_currency]
    
    # Then convert from the base currency to the target currency
    converted_amount = base_amount * exchange_rates[to_currency]
    
    return converted_amount
# Example usage:
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.0,
    'GBP': 0.75
}

amount = 100  # Amount in USD
from_currency = 'EUR'
to_currency = 'JPY' 
converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
# Note: In a real-world scenario, exchange rates would be fetched from an online API.
