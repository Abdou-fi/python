import pandas as pd      #Now Pandas is imported and ready to use, pd is the alias

mydataset = {
  'car': ["BMW", "Volvo", "Ford"],
  'year': [1997, 2019, 2020]
}
print("\n ==========================================\n")

print(mydataset)

print("\n ==========================================\n")

my_data = pd.DataFrame(mydataset)
print(my_data)

print("\n ==========================================\n")

