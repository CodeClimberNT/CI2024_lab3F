import heapq
import networkx as nx


def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, None))
    closed_set = set()
    came_from = {}

    while open_set:
        _, cost_so_far, current, parent = heapq.heappop(open_set)

        if current in closed_set:
            continue

        came_from[current] = parent

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path

        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
            estimated_cost = cost_so_far + cost + heuristic(neighbor, goal)
            heapq.heappush(open_set, (estimated_cost, cost_so_far + cost, neighbor, current))

    return None  # Path not found


def heuristic(node, goal):
    return abs(node - goal)


def get_neighbors(node):
    graph = {1: [(2, 1), (3, 4)], 2: [(3, 2), (4, 5)], 3: [(4, 1)], 4: []}
    G = nx.Graph()
    G.add_weighted_edges_from(
        [
            (1, 2, 1),
            (1, 3, 4),
            (2, 3, 2),
            (2, 4, 5),
            (3, 4, 1),
        ]
    )

    graph = {node: [(neighbor, data['weight']) for neighbor, data in G.adj[node].items()] for node in G.nodes}
    return graph.get(node, [])


# Test the A* algorithm
start_node = 1
goal_node = 4
path = a_star(start_node, goal_node, get_neighbors, heuristic)
print(f"Shortest path from {start_node} to {goal_node}: {path}")
