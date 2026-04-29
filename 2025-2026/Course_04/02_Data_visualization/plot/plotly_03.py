import plotly.express as px
import bokeh.plotting as bp
from bokeh.models import HoverTool

# Create a new plot
p = bp.figure(plot_width=700, plot_height=400, title="Interactive Plot", tools="pan,wheel_zoom,box_zoom,reset")
# Add a scatter plot to the figure
p.scatter([1, 2, 3, 4, 5], [10, 15, 25, 30, 35])
# Show the plot
bp.show(p)