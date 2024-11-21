import heapq
def uniform_cost_search(weighted_graph, source):
    queue = [(0, source)]
    cost = {node: float('inf') for node in weighted_graph}
    cost[source] = 0
    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_cost > cost[current_node]:
            continue
        for neighbor, edge_cost in weighted_graph[current_node]:
            new_cost = current_cost + edge_cost
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return cost
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("Uniform Cost Search from 'A':", uniform_cost_search(weighted_graph, 'A'))
