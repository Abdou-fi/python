from forex_python.converter import CurrencyRates 
c = CurrencyRates() 
amount = 1 
from_currency = 'USD' 
to_currency = 'INR' 
converted_amount = c.convert(from_currency, to_currency, amount) 
print(amount, from_currency, "=", converted_amount, to_currency)