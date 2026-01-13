from decimal import Decimal, getcontext, localcontext, ROUND_DOWN

# TWOPLACES = Decimal('0.01') # Defines the fixed-point format (two decimal places)

number = 0.287

with localcontext() as ctx:
    ctx.rounding = ROUND_DOWN
    d = Decimal(number).quantize(Decimal('0.01'))
    x= Decimal('2.3399').quantize(d)
    print(x)  # Outputs: 2.99
    
print(x * 1000)