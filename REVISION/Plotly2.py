import plotly.graph_objects as go

# Define the vertices of the triangle
x = [0, 1, 0.5]
y = [0, 0, 1]
z = [0, 0, 1]

# Create a 3D scatter plot for the vertices
points = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode="markers+text",
    marker=dict(size=5, color="red"),
    text=["A", "B", "C"],
    textposition="top center",
)

# Create a mesh to connect the vertices into a triangle
triangle = go.Mesh3d(
    x=x,
    y=y,
    z=z,
    i=[0],
    j=[1],
    k=[2],  # indices of vertices forming the triangle
    color="lightblue",
    opacity=0.50,
)

# Combine into a figure
fig = go.Figure(data=[points, triangle])

# Set layout for better visualization
fig.update_layout(
    scene=dict(xaxis=dict(title="X"), yaxis=dict(title="Y"), zaxis=dict(title="Z")),
    title="3D Triangle Visualization",
)
fig.show()
