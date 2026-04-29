# Bar graph plot using different Python libraries
# 2. Plotly
import plotly.express as px
categories = ['A','B', 'C', 'D']
values = [25, 40, 30, 20]

# Create an interactive bar chart
px.bar(x=categories, y=values, labels={'x':'Categories', 'y':'Values'}, title='Bar Chart example')
px.show()