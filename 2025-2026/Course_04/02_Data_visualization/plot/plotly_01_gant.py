import plotly.express as px
import pandas as pd
import datetime as dt

df = pd.DataFrame([
    dict(Task="Project Planning", Start='2025-01-10', Finish='2025-02-15'),
    dict(Task="Development", Start='2025-02-15', Finish='2025-03-01'),
    dict(Task="Testing", Start='2025-03-01', Finish='2025-03-05'),
    dict(Task="Launch", Start='2025-03-05', Finish='2025-03-10')
])

df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
fig.update_yaxes(autorange="reversed") # optional: tasks are listed from top to bottom
fig.show()
