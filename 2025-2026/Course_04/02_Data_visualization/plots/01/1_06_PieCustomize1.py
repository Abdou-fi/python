import matplotlib.pyplot as plt
import seaborn as sns
age_group_labels = [
    'Children 0-18', 'Adults 19-25', 'Adults 26-34',
    'Adults 35-54', 'Adults 55-64', 'Seniors 65+'
]
age_group_populations = [
    75_307_800, 27_799_100, 39_817_700,
    81_478_600, 42_061_700, 52_784_400
]
sns.set(font_scale=1.2)
plt.figure(figsize=(8, 8))

plt.pie(
    x=age_group_populations,
    labels=age_group_labels,
    autopct='%1.2f%%',
    colors=sns.color_palette('Set2'),
    startangle=90,
    # Add space around only one slice
    explode=[0, 0, 0, 0, 0.12, 0]
)
plt.legend()
plt.show()




