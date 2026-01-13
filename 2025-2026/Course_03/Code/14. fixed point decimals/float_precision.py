print(0.1 + 0.2 == 0.3)  # Outputs: False
print(0.1 + 0.2)

print(0.1 + 0.3 == 0.4)  # Outputs: True
print(0.1 + 0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # Outputs: True