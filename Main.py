import tkinter
import random
import GraphDisplay
from SpatialGraphGenerator import generate_grid_graph
from Graph import Graph


graph = Graph(generate_grid_graph(grid_dimensions=(1000, 700), origin=(50, 50), spacing=50))

GraphDisplay.draw_spatial_graph(graph)
