import heapq
import copy

# Target configuration for the 8-puzzle
TARGET_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Utility functions to calculate heuristic values
def h1(_):
    return 0

def h2(state):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != TARGET_STATE[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

def h3(state):
    manhattan_distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = divmod(tile - 1, 3)
                manhattan_distance += abs(i - goal_i) + abs(j - goal_j)
    return manhattan_distance

def h4(_):
    # An inadmissible heuristic: artificially large value for demonstration
    return 100

# A* Search algorithm
def a_star_search(initial_state, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state))
    visited = set()
    g_score = {str(initial_state): 0}
    moves = 0

    while priority_queue:
        moves += 1
        _, current = heapq.heappop(priority_queue)
        
        if current == TARGET_STATE:
            return g_score[str(current)], moves
        
        visited.add(str(current))
        x, y = find_zero(current)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                neighbor = copy.deepcopy(current)
                neighbor[x][y], neighbor[new_x][new_y] = neighbor[new_x][new_y], neighbor[x][y]
                
                if str(neighbor) in visited:
                    continue
                
                tentative_g_score = g_score[str(current)] + 1
                if tentative_g_score < g_score.get(str(neighbor), float('inf')):
                    g_score[str(neighbor)] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor)
                    heapq.heappush(priority_queue, (f_score, neighbor))
                    
    return None, moves

# Find position of the empty tile (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Display function for the puzzle
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Initial puzzle state example (can be changed)
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Run A* with different heuristics
print("Initial State:")
print_puzzle(initial_state)

for i, heuristic in enumerate([h1, h2, h3, h4], start=1):
    print(f"Running A* Search with Heuristic h{i}")
    cost, moves = a_star_search(initial_state, heuristic)
    if cost is not None:
        print(f"Solution found with cost: {cost}, Total moves: {moves}\n")
    else:
        print("No solution found.\n")
