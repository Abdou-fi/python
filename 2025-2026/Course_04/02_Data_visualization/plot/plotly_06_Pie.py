import plotly.express as px
labels = ['Category A', 'Category B', 'Category C', 'Category D']
values= [15, 30, 45, 10]
fig = px.pie(names=labels, values=values, title='My Pie Chart')
fig.show()