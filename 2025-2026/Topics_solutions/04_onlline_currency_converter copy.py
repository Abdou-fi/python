# online_currency_converter using yfinance for exchange rates and a list of currencies

import yfinance as yf
def convert_currency(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another using yfinance for exchange rates.

    :param amount: The amount of money to convert.
    :param from_currency: The currency code of the original currency.
    :param to_currency: The currency code of the target currency.
    :return: The converted amount in the target currency.
    """
    if from_currency == to_currency:
        return amount

    # Fetch exchange rates using yfinance
    pair = f"{from_currency}{to_currency}=X"
    data = yf.Ticker(pair)
    hist = data.history(period="1d")
    
    if hist.empty:
        raise ValueError("Invalid currency code provided or unable to fetch exchange rate.")

    exchange_rate = hist['Close'][0]

    # Convert the amount
    converted_amount = amount * exchange_rate
    
    return converted_amount

# Example usage:
amount = 100  # Amount in from_currency
from_currency = 'EUR'
to_currency = 'JPY' 
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")