
from collections import deque
def is_valid_state(state):
    F, W, G, C = state
    # Check if the farmer is not leaving the wolf with the goat or the goat with the cabbage
    if (W == G != F) or (G == C != F):
        return False
    return True
def solve_wgc_problem():
    # Initial state: all on the left bank
    initial_state = (0, 0, 0, 0)  # (Farmer, Wolf, Goat, Cabbage)
    goal_state = (1, 1, 1, 1)     # Goal state: all on the right bank

    # Queue for BFS: each element is (current_state, path_taken)
    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])  # To keep track of visited states

    # BFS
    while queue:
        current_state, path = queue.popleft()
        
        # If we've reached the goal state, return the path
        if current_state == goal_state:
            return path

        F, W, G, C = current_state
        
        # Possible moves (0->1 for crossing right, 1->0 for crossing left)
        possible_moves = [
            (1 - F, W, G, C),        # Farmer crosses alone
            (1 - F, 1 - W, G, C) if F == W else None,  # Farmer takes the wolf
            (1 - F, W, 1 - G, C) if F == G else None,  # Farmer takes the goat
            (1 - F, W, G, 1 - C) if F == C else None   # Farmer takes the cabbage
        ]
        for new_state in possible_moves:
            if new_state and new_state not in visited and is_valid_state(new_state):
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None  # If no solution is found
solution = solve_wgc_problem()
if solution:
    print("Solution steps to transport the wolf, goat, and cabbage safely:")
    for step in solution:
        F, W, G, C = step
        print(f"Farmer: {'Right' if F else 'Left'}, Wolf: {'Right' if W else 'Left'}, "
              f"Goat: {'Right' if G else 'Left'}, Cabbage: {'Right' if C else 'Left'}")
else:
    print("No solution found.")
