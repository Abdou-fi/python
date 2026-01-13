# The program will keep asking for a valid quantity until the user enters a valid number.
balance=45678.67
while True:
    try: 
        num = float(input('Deposit: ')) 
        break 
    except ValueError: 
        print('Must be a valid quantity.')

balance += num 
print(f'Balance: {balance}')
