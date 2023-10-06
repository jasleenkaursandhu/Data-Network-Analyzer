import os
import matplotlib.pyplot as plt

def handshaking_theorem(e):
    # The Handshaking Theorem states that in any graph, the sum of degrees of all nodes is twice the number of edges.
    return 2 * e

# Input the number of edges in your graph
num_edges = int(input("Enter the number of edges in the graph: "))

# Calculate the sum of degrees using the Handshaking Theorem
sum_of_degrees = handshaking_theorem(num_edges)

# Explain the Handshaking Theorem
print("The Handshaking Theorem states that in any graph:")
print("- The sum of degrees of all nodes is twice the number of edges.")
print("- It's a fundamental property of graphs and often used in graph theory.")

# Create a bar chart visualization to illustrate the Handshaking Theorem
nodes = [f"Node {i}" for i in range(1, num_edges * 2 + 1)]
degrees = [1] * (num_edges * 2)

plt.figure(figsize=(10, 5))
plt.bar(nodes, degrees, color='skyblue')
plt.xlabel("Nodes")
plt.ylabel("Degree")
plt.title("Visualization of the Handshaking Theorem")
plt.xticks(rotation=45)
plt.tight_layout()

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Save the visualization to the "images" folder
image_path = os.path.join("images", "handshaking_theorem_visualization.png")
plt.savefig(image_path)

# Display the sum of degrees
print(f"The sum of degrees is: {sum_of_degrees}")

# Show the visualization
plt.show()
