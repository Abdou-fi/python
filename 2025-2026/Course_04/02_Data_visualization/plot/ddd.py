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




# import plotly.express as px
# from sympy import python # Import Plotly Express for simpler interactive plotting
# # Sample Data 
# df = px.data.iris() # Load built-in Iris dataset
# # Create Interactive Scatter Plot 
# fig = px.scatter(df, x='sepal_width', y="sepal_length", color='species',  title="Interactive Scatter Plot Example")  # Create an interactive scatter plot
                                      
# fig.show() # Display the interactive plot



# # Candlestick Chart plot using in Python
# import yfinance as yf
# import plotly.graph_objects as go
# # Download historical data for Apple Inc. (AAPL)
# data = yf.download('AAPL', start='2025-01-01', end='2025-12-31')
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

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

try:
    # Try to fetch a list of Matplotlib releases and their dates
    # from https://api.github.com/repos/matplotlib/matplotlib/releases
    import json
    import urllib.request

    url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    url += '?per_page=100'
    data = json.loads(urllib.request.urlopen(url, timeout=1).read().decode())

    dates = []
    releases = []
    for item in data:
        if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
            dates.append(item['published_at'].split("T")[0])
            releases.append(item['tag_name'].lstrip("v"))

except Exception:
    # In case the above fails, e.g. because of missing internet connection
    # use the following lists as fallback.
    releases = ['2.2.4', '3.0.3', '3.0.2', '3.0.1', '3.0.0', '2.2.3',
                '2.2.2', '2.2.1', '2.2.0', '2.1.2', '2.1.1', '2.1.0',
                '2.0.2', '2.0.1', '2.0.0', '1.5.3', '1.5.2', '1.5.1',
                '1.5.0', '1.4.3', '1.4.2', '1.4.1', '1.4.0']
    dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
             '2014-10-26', '2014-10-18', '2014-08-26']

dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]  # Convert strs to dates.
releases = [tuple(release.split('.')) for release in releases]  # Split by component.
dates, releases = zip(*sorted(zip(dates, releases)))  # Sort by increasing date.
# Choose some nice levels: alternate meso releases between top and bottom, and
# progressively shorten the stems for micro releases.
levels = []
macro_meso_releases = sorted({release[:2] for release in releases})
for release in releases:
    macro_meso = release[:2]
    micro = int(release[2])
    h = 1 + 0.8 * (5 - micro)
    level = h if macro_meso_releases.index(macro_meso) % 2 == 0 else -h
    levels.append(level)


def is_feature(release):
    """Return whether a version (split into components) is a feature release."""
    return release[-1] == '0'


# The figure and the axes.
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

# The vertical stems.
ax.vlines(dates, 0, levels,
          color=[("tab:red", 1 if is_feature(release) else .5) for release in releases])
# The baseline.
ax.axhline(0, c="black")
# The markers on the baseline.
meso_dates = [date for date, release in zip(dates, releases) if is_feature(release)]
micro_dates = [date for date, release in zip(dates, releases)
               if not is_feature(release)]
ax.plot(micro_dates, np.zeros_like(micro_dates), "ko", mfc="white")
ax.plot(meso_dates, np.zeros_like(meso_dates), "ko", mfc="tab:red")

# Annotate the lines.
for date, level, release in zip(dates, levels, releases):
    version_str = '.'.join(release)
    ax.annotate(version_str, xy=(date, level),
                xytext=(-3, np.sign(level)*3), textcoords="offset points",
                verticalalignment="bottom" if level > 0 else "top",
                weight="bold" if is_feature(release) else "normal",
                bbox=dict(boxstyle='square', pad=0, lw=0, fc=(1, 1, 1, 0.7)))

ax.xaxis.set(major_locator=mdates.YearLocator(),
             major_formatter=mdates.DateFormatter("%Y"))

# Remove the y-axis and some spines.
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()

