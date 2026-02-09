age = 25

if age < 18:
    status1 = "Too Young"
elif age == 18:
    status1 = "Still too Young"
elif 18 < age < 20:
    status1 = "Old enough now"
elif 20 <= age < 40:
    status1 = "Perfect"
else:
    status1 = "Welcome"

print(status1)

status2 ={
    (age < 18): "Too Young", 
    (age == 18): "Still too Young", 
    (18 < age < 20): "Old enough now", 
    (20 <= age < 40): "Perfect", 
    (age >= 40): "Welcome",
}[True]

print(status2)