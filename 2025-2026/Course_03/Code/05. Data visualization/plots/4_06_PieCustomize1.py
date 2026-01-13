import matplotlib.pyplot as plt
import seaborn as sns
age_group_labels = [
    'Children 0-18', 'Adults 19-25', 'Adults 26-34',
    'Adults 35-54', 'Adults 55-64', 'Seniors 65+'
]
age_group_populations = [
    75307800, 27799100, 39817700, 
    81478600, 42061700, 52784400
]
# print age groups and corresponding populations 
for label, population in zip(age_group_labels, age_group_populations):
    print (f'{label}:    {population:,}')


