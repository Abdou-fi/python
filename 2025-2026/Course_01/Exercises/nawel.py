import cmath
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b**2 - 4 * a * c
print(f"Δ = {delta}")
if delta > 0:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print("الحلول في الأعداد الحقيقية: ")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"الحل في الأعداد الحقيقية (جذر مضاعف): x = {x}")
else:
    print("لا يوجد حلول في الأعداد الحقيقية لأن المحدد سالب.")
x1_complex = (-b + cmath.sqrt(delta)) / (2 * a)
x2_complex = (-b - cmath.sqrt(delta)) / (2 * a)
print("الحلول في الأعداد المركبة: ")
print(f"x1 = {x1_complex}")
print(f"x2 = {x2_complex}")