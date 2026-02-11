# Grouped Bar Graph using Matplotlib in Python

import matplotlib.pyplot as pl
BAR_WIDTH = 0.4
# set up grouped bar charts
teama_results = (60, 75, 56, 62, 58)
teamb_results = (55, 68, 88, 73, 55)
# Set up the index for each bar
index_teama = (1, 2, 3, 4, 5)
index_teamb = [i + BAR_WIDTH for i in index_teama]
# Determine the mid point for the ticks
ticks = [i + BAR_WIDTH / 2 for i in index_teama]
tick_labels = ('Lab1', 'Lab2', 'Lab 3', 'Lab 4', 'Lab 5')
# Plot the bar charts
pl.bar(index_teama, teama_results, BAR_WIDTH, color='pink', label='Team A')
pl.bar(index_teamb, teamb_results, BAR_WIDTH, color='g', label='Team B')
# Set up the graph
pl.xlabel('Labs')
pl.ylabel('Scores')
pl.title('Scores by Lab')
pl.xticks(ticks, tick_labels)
pl.legend()
# Display the graph
pl.show()