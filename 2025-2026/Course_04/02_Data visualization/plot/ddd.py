# import plotly.express as px

# # Sample data
# data = {
#     "id": ["A", "B", "C", "D", "E", "F"],
#     "parent": ["", "A", "A", "B", "B", "C"],
#     "value": [16, 25, 7, 8, 12, 6]
# }
# # Create a sunburst chart 
# fig = px.sunburst(data, names='id', parents='parent', values='value' )

# # Set the chart title 
# fig.update_layout(title_text="Sunburst Chart")

# # Show the chart
# fig.show() 

# import yfinance as yf
# import plotly.graph_objects as go
# # Download historical data for Apple Inc. (AAPL)
# data = yf.download('AAPL', start='2023-01-01', end='2025-12-31')
# # Create a candlestick chart
# fig = go.Figure(data=[go.Candlestick(x=data.index,
#                 open=data['Open'],
#                 high=data['High'],
#                 low=data['Low'],
#                 close=data['Close'])])

# # Set the chart title
# fig.update_layout(title_text='AAPL Candlestick Chart')

# # Show the chart
# fig.show()



# import plotly.express as px
# import bokeh.plotting as bp
# from bokeh.models import HoverTool

# # Create a new plot
# p = bp.figure(plot_width=700, plot_height=400, title="Interactive Plot", tools="pan,wheel_zoom,box_zoom,reset")
# # Add a scatter plot to the figure
# p.scatter([1, 2, 3, 4, 5], [10, 15, 25, 30, 35])
# # Show the plot
# bp.show(p)




import plotly.express as px # Import Plotly Express for simpler interactive plotting
# Sample Data 
df = px.data.iris() # Load built-in Iris dataset
# Create Interactive Scatter Plot 
fig = px.scatter(df, x='sepal_width', y="sepal_length", color='species',  title="Interactive Scatter Plot Example")  # Create an interactive scatter plot
                                      
fig.show() # Display the interactive plot



# Candlestick Chart plot using in Python
import yfinance as yf
import plotly.graph_objects as go
# Download historical data for Apple Inc. (AAPL)
data = yf.download('AAPL', start='2025-01-01', end='2025-12-31')
# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

# Set the chart title
fig.update_layout(title_text='AAPL Candlestick Chart')

# Show the chart
fig.show()