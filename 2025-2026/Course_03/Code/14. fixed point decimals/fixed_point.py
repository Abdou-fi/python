from decimal import Decimal, getcontext, localcontext, ROUND_DOWN

TWOPLACES = Decimal('0.01') # Defines the fixed-point format (two decimal places)

number = 0.287

with localcontext() as ctx:
    ctx.rounding = ROUND_DOWN
    d1 = Decimal(number).quantize(TWOPLACES)
    d2 = Decimal(str(number*100)).quantize(TWOPLACES)
    print(d1)  # Outputs: 2.99
    
print(d1 * 1000, d2)