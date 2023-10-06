import networkx as nx
import matplotlib.pyplot as plt
import os

class FamilyTree:
    def __init__(self, num_people):
        self.num_people = num_people

    def min_in_degree(self):
        return 1  # Minimum in-degree is 1 in a family tree

    def max_in_degree(self):
        return 2  # Maximum in-degree is typically 2 for biological parents

    def min_out_degree(self):
        return 0  # Minimum out-degree is 0 if not all individuals become parents

    def max_out_degree(self):
        return self.num_people - 1  # Maximum out-degree can be n-1

    def has_self_loops(self):
        return False  # Self-loops are not possible in a family tree

    def visualize_family_tree(self, save_path=None):
        # Create a directed graph representing the family tree
        G = nx.DiGraph()

        # Add nodes to the graph
        G.add_nodes_from(range(self.num_people))

        # Add edges to represent family relationships
        for i in range(self.num_people):
            # Connect individuals to their parents (assuming a binary family tree)
            if i > 0:
                G.add_edge((i - 1) // 2, i)

        # Plot the family tree
        pos = nx.spring_layout(G, seed=42)
        labels = {i: f"Person {i}" for i in range(self.num_people)}
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue')
        plt.title("Family Tree Visualization")

        # Save the visualization as an image if save_path is provided
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

if __name__ == "__main__":
    num_people = int(input("Enter the number of people in the family tree: "))
    family_tree = FamilyTree(num_people)

    print("1. Minimum in-degree of a node:", family_tree.min_in_degree())
    print("2. Maximum in-degree of a node:", family_tree.max_in_degree())
    print("3. Minimum out-degree of a node:", family_tree.min_out_degree())
    print("4. Maximum out-degree of a node:", family_tree.max_out_degree())
    print("5. Are self-loops possible in this tree?", "Yes" if family_tree.has_self_loops() else "No")

    # Create the 'images' folder if it doesn't exist
    os.makedirs("images", exist_ok=True)

    # Visualize the family tree and save it as "family_tree.png" in the 'images' folder
    family_tree.visualize_family_tree(save_path="images/family_tree.png")
