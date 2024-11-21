import random

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(goal_state)}  # Position map for Manhattan distance

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def h1_displaced_tiles(state):
    return sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != 0)

def h2_manhattan_distance(state):
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            goal_x, goal_y = goal_positions[tile]
            current_x, current_y = i // 3, i % 3
            distance += abs(goal_x - current_x) + abs(goal_y - current_y)
    return distance

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    x, y = index // 3, index % 3
    moves = {'Up': (x - 1, y), 'Down': (x + 1, y), 'Left': (x, y - 1), 'Right': (x, y + 1)}
    
    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = state[:]
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(new_state)
    return neighbors

def hill_climbing(start_state, heuristic):
    current_state = start_state
    current_cost = heuristic(current_state)
    iterations = 0  # Track the number of steps taken

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_cost = float('inf')

        for neighbor in neighbors:
            cost = heuristic(neighbor)
            if cost < next_cost:
                next_state, next_cost = neighbor, cost

        if next_cost >= current_cost:
            break
        current_state, current_cost = next_state, next_cost
        iterations += 1  # Increment step count

    return current_state, current_cost, iterations

def generate_random_start():
    state = goal_state[:]
    random.shuffle(state)
    return state

start_state = generate_random_start()
print("Start State:")
display(start_state)

# Using Heuristic h1 (Displaced Tiles)
print("Using Heuristic h1 (Displaced Tiles):")
final_state, final_cost, steps = hill_climbing(start_state, h1_displaced_tiles)
display(final_state)
print("Final Cost (Displaced Tiles):", final_cost)
print("Steps Taken:", steps)

# Using Heuristic h2 (Manhattan Distance)
print("Using Heuristic h2 (Manhattan Distance):")
final_state, final_cost, steps = hill_climbing(start_state, h2_manhattan_distance)
display(final_state)
print("Final Cost (Manhattan Distance):", final_cost)
print("Steps Taken:", steps)
