import plotly.express as px # Import Plotly Express for simpler interactive plotting
# Sample Data
df = px.data.iris() # Load built-in Iris dataset
# Create Interactive Scatter Plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',   # Create an interactive scatter plot
        title="Interactive Scatter Plot Example") # Add a title to the plot
fig.show() # Display the interactive plot