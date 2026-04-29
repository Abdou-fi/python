import plotly.graph_objects as go
stages = ["Sent", "Viewed", "clicked", "add to cart","purchased"] 
values = [1000, 700, 400, 200, 100]
fig = go.Figure(go.Funnel(
    y=stages, 
    x=values
))
fig.update_layout(title="website Conversion Funnel")
fig.show()