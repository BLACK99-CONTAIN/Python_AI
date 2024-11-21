import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)]
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    f_costs = {node: float('inf') for node in graph}
    f_costs[start] = heuristic[start]
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_costs[goal]

        for neighbor, weight in graph[current]:
            tentative_g_cost = g_costs[current] + weight
            if tentative_g_cost < g_costs[neighbor]:
                came_from[neighbor] = current
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (f_costs[neighbor], neighbor))

    return None, float('inf')
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 4)],
    'C': [('A', 3), ('E', 1)],
    'D': [('B', 1), ('E', 1), ('F', 2)],
    'E': [('B', 4), ('C', 1), ('D', 1), ('F', 3)],
    'F': [('D', 2), ('E', 3)]
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0  # Goal node heuristic is 0
}
start_node = 'A'
goal_node = 'F'
path, cost = a_star(graph, start_node, goal_node, heuristic)
print("Shortest path:", path)
print("Total cost:", cost)
