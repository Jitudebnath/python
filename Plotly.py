import plotly.express as px

# Sample data
data = {"x": [1, 2, 3, 4, 5], "y": [10, 15, 13, 17, 20]}

# Create a line plot
fig = px.line(data, x="x", y="y", title="Test Plotly Line Chart")

# Show the plot
fig.show()
