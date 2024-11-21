import random
import math

# Define the goal state and possible moves
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(goal_state)}  # Position map for Manhattan distance

def display(state):
    """Display the puzzle state in a 3x3 grid format."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def h1_displaced_tiles(state):
    """Heuristic 1: Number of misplaced tiles."""
    return sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != 0)

def h2_manhattan_distance(state):
    """Heuristic 2: Total Manhattan distance."""
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            goal_x, goal_y = goal_positions[tile]
            current_x, current_y = i // 3, i % 3
            distance += abs(goal_x - current_x) + abs(goal_y - current_y)
    return distance

def get_neighbors(state):
    """Generate possible moves (neighbors) by moving the blank tile."""
    neighbors = []
    index = state.index(0)  # Blank tile position
    x, y = index // 3, index % 3

    # Define move directions (Up, Down, Left, Right)
    moves = {'Up': (x - 1, y), 'Down': (x + 1, y), 'Left': (x, y - 1), 'Right': (x, y + 1)}
    
    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check bounds
            new_index = new_x * 3 + new_y
            new_state = state[:]
            # Swap blank with the target tile
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(new_state)
    return neighbors

def simulated_annealing(start_state, initial_temp=1000, cooling_rate=0.95, max_iterations=10000, heuristic=h2_manhattan_distance):
    """Simulated Annealing Search Algorithm."""
    current_state = start_state
    current_cost = heuristic(current_state)
    
    temperature = initial_temp

    for iteration in range(max_iterations):
        if current_cost == 0:  # Goal state reached
            break

        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_cost = heuristic(next_state)

        # If the next state is better, move to it
        if next_cost < current_cost:
            current_state, current_cost = next_state, next_cost
        else:
            # Calculate probability of acceptance of worse state
            acceptance_probability = math.exp((current_cost - next_cost) / temperature)
            if random.random() < acceptance_probability:
                current_state, current_cost = next_state, next_cost

        # Cool down the temperature
        temperature *= cooling_rate

    return current_state, current_cost

# Generate a random starting state for testing
def generate_random_start():
    state = goal_state[:]
    random.shuffle(state)
    return state

# Example usage
start_state = generate_random_start()
print("Start State:")
display(start_state)

# Simulated Annealing with Heuristic 1 (Displaced Tiles)
print("Using Heuristic h1 (Displaced Tiles):")
final_state, final_cost = simulated_annealing(start_state, heuristic=h1_displaced_tiles)
display(final_state)
print("Final Cost (Displaced Tiles):", final_cost)

# Simulated Annealing with Heuristic 2 (Manhattan Distance)
print("Using Heuristic h2 (Manhattan Distance):")
final_state, final_cost = simulated_annealing(start_state, heuristic=h2_manhattan_distance)
display(final_state)
print("Final Cost (Manhattan Distance):", final_cost)
