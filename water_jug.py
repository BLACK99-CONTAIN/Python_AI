from collections import deque
def water_jug_bfs(target, jug1_capacity=4, jug2_capacity=3):
    queue = deque([((0, 0), [])])
    visited = set()  # To keep track of visited states
    while queue:
        (jug1, jug2), path = queue.popleft()
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        queue.append(((jug1_capacity, jug2), path + [(jug1, jug2)]))
        queue.append(((jug1, jug2_capacity), path + [(jug1, jug2)]))
        queue.append(((0, jug2), path + [(jug1, jug2)]))
        queue.append(((jug1, 0), path + [(jug1, jug2)]))
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append(((jug1 - pour_to_jug2, jug2 + pour_to_jug2), path + [(jug1, jug2)]))
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append(((jug1 + pour_to_jug1, jug2 - pour_to_jug1), path + [(jug1, jug2)]))

    return None  # If there's no solution (shouldn't happen for this problem)
target_amount = 2
solution_path = water_jug_bfs(target_amount)
if solution_path:
    print("Steps to measure exactly 2 liters:")
    for step in solution_path:
        print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")
else:
    print("No solution found.")
