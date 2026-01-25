# Currency Converter: Build a converter that asks for exchange rates and converts between different currencies.

def get_currencies_to_convert():
    currencies = {}
    currencies["from"] = input("Enter the currencies to convert from: ")
    currencies["to"] = input("Enter the currencies to convert to: ")
    return currencies

def get_exchange_rate():
    try:
        rate = float(input("Enter the exchange rate: "))
        return rate
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_exchange_rate()

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Currency Converter")
    print("------------------")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    rate = get_exchange_rate()
    converted_amount = convert_currency(amount, rate)
    currencies = get_currencies_to_convert()
    print(f"{amount} {currencies["from"]} is equal to {converted_amount} {currencies["to"]}.")

if __name__ == "__main__":
    main()