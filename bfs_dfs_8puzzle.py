from collections import deque, defaultdict

# Graph class to store the adjacency list of multiple graphs
class Graph:
    def __init__(self):
        self.graphs = defaultdict(dict)  # Stores multiple graphs by names

    def add_edge(self, graph_name, start, end):
        if graph_name not in self.graphs:
            self.graphs[graph_name] = defaultdict(list)
        self.graphs[graph_name][start].append(end)
        self.graphs[graph_name][end].append(start)  # Assuming undirected graph

    def bfs(self, graph_name, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graphs[graph_name][node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs(self, graph_name, start):
        visited = set()
        result = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in reversed(self.graphs[graph_name][node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def add_example_graphs(self):
        self.add_edge("Graph1", "A", "B")
        self.add_edge("Graph1", "A", "C")
        self.add_edge("Graph1", "B", "D")
        self.add_edge("Graph1", "C", "D")
        self.add_edge("Graph1", "D", "E")

        self.add_edge("Graph2", "1", "2")
        self.add_edge("Graph2", "1", "3")
        self.add_edge("Graph2", "2", "4")
        self.add_edge("Graph2", "3", "5")
        self.add_edge("Graph2", "5", "6")

        self.add_edge("Graph3", "X", "Y")
        self.add_edge("Graph3", "X", "Z")
        self.add_edge("Graph3", "Y", "W")
        self.add_edge("Graph3", "Z", "W")
        self.add_edge("Graph3", "W", "V")

if __name__ == "__main__":
    g = Graph()
    g.add_example_graphs()

    for graph_name in g.graphs.keys():
        print(f"\n{graph_name} - BFS and DFS Traversal from Start Node:")
        
        # Perform BFS and DFS for each graph with a start node
        start_node = list(g.graphs[graph_name].keys())[0]
        bfs_result = g.bfs(graph_name, start_node)
        dfs_result = g.dfs(graph_name, start_node)

        print(f"Start Node: {start_node}")
        print("BFS Traversal:", bfs_result)
        print("DFS Traversal:", dfs_result)
