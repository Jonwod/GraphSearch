import Search
import random
from GraphDisplay import GraphDisplay
from SpatialGraphGenerator import generate_grid_graph
from Graph import Graph


graph = Graph(generate_grid_graph(grid_dimensions=(1000, 700), origin=(50, 50), spacing=100, min_connections=2, max_connections = 4))

start = graph.nodes[random.randint(0, len(graph.nodes) - 1)]
goal = graph.nodes[random.randint(0, len(graph.nodes) - 1)]

print("start: " + str(start.id) + "   goal: " + str(goal.id))

path = Search.depth_first(start, goal)

display = GraphDisplay(graph, path=path)

if path is None:
    print("No path between " + str(start.id) + " and " + str(goal.id))
else:
    display.highlight_path(path)
