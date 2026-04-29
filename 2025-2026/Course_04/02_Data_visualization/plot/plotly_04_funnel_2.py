import plotly.graph_objects as go
stages = ["Sent", "Viewed", "clicked", "add to cart","purchased"] 
values = [2000, 1400, 800, 400, 200]
fig = go.Figure(go.Funnel(
    y=stages, 
    x=values,
    textinfo="value+percent initial"
))
fig.update_layout(
    title="Funnel Chart Example",
    title_x=0.5
)
fig.show()