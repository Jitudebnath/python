import matplotlib.pyplot as plt
import networkx as nx

# Define flow chart steps
steps = [
    ("Start", "Install matplotlib"),
    ("Install matplotlib", "Create Python file"),
    ("Create Python file", "Import matplotlib.pyplot"),
    ("Import matplotlib.pyplot", "Write plotting code"),
    ("Write plotting code", "Run program"),
    ("Run program", "Plot window opens"),
    ("Plot window opens", "End"),
]

# Create directed graph
G = nx.DiGraph()
G.add_edges_from(steps)

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)  # Layout for nodes

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
    arrowstyle="->",
    arrowsize=20,
)

plt.title("Flow Chart: Using Matplotlib in VS Code", fontsize=14)
plt.show()
