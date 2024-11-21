import math

class Node:
    def __init__(self, name, is_and_node=False, heuristic=math.inf):
        self.name = name                    # Name of the node (e.g., 'A', 'B', 'C')
        self.is_and_node = is_and_node      # If True, this node is an AND node; otherwise, it’s an OR node
        self.heuristic = heuristic          # Heuristic value for this node (initially high for non-leaf nodes)
        self.children = []                  # List of child nodes (with path cost)
        self.optimal_child = None           # Optimal child to follow in case of an OR node
        self.solved = False                 # True if this node is considered solved

    def add_child(self, child, cost=1):
        self.children.append((child, cost))

    def __repr__(self):
        return f"Node({self.name}, H={self.heuristic})"

def ao_star(node, path_cost=0):
    if node.solved:  # If the node is already solved, return its heuristic
        return node.heuristic

    if not node.children:  # Leaf node; assume its heuristic is the end cost
        node.solved = True
        return node.heuristic

    costs = []

    if node.is_and_node:
        total_cost = 0  # AND node: sum of all child costs
        all_children_solved = True
        for child, cost in node.children:
            child_cost = ao_star(child, path_cost + cost)
            total_cost += cost + child_cost
            if not child.solved:
                all_children_solved = False
        node.heuristic = total_cost
        node.solved = all_children_solved

    else:
        min_cost = math.inf
        optimal_child = None
        for child, cost in node.children:
            child_cost = ao_star(child, path_cost + cost)
            total_cost = cost + child_cost
            if total_cost < min_cost:
                min_cost = total_cost
                optimal_child = child
        node.heuristic = min_cost
        node.optimal_child = optimal_child
        node.solved = node.optimal_child.solved if node.optimal_child else False

    return node.heuristic

# Define nodes
A = Node("A")                # Root OR node
B = Node("B", is_and_node=True)    # AND node
C = Node("C")                # OR node
D = Node("D")                # Leaf node with heuristic
E = Node("E")                # Leaf node with heuristic
F = Node("F", heuristic=2)   # Leaf node with heuristic
G = Node("G", heuristic=4)   # Leaf node with heuristic
H = Node("H", heuristic=1)   # Leaf node with heuristic
I = Node("I", heuristic=3)   # Leaf node with heuristic

# Construct tree by adding children and specifying path costs
A.add_child(B, cost=1)       # A -> B (cost 1)
A.add_child(C, cost=3)       # A -> C (cost 3)
B.add_child(D, cost=1)       # B (AND) -> D (cost 1)
B.add_child(E, cost=1)       # B (AND) -> E (cost 1)
C.add_child(F, cost=2)       # C -> F (cost 2)
C.add_child(G, cost=4)       # C -> G (cost 4)
D.add_child(H, cost=1)       # D -> H (cost 1)
E.add_child(I, cost=3)       # E -> I (cost 3)

# Run AO* algorithm on the root node A
print("Running AO* Algorithm on the AND-OR Tree...")
solution_cost = ao_star(A)
print(f"Optimal Solution Cost: {solution_cost}")
print(f"Root Node Heuristic after AO*: {A.heuristic}")
