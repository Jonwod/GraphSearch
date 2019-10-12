import random
from SpatialNode import SpatialNode


def generate_disconnected_node_grid(grid_dimensions=(1200, 800), spacing=40, origin=(0, 0)):
    columns = int(grid_dimensions[0]) // spacing
    rows = int(grid_dimensions[1]) // spacing
    grid = []
    for x in range(0, columns):
        # Add column
        grid.append([])
        for y in range(0, rows):
            pos = (origin[0] + x*spacing, origin[1] + y*spacing)
            grid[x].append(SpatialNode(pos))
    return grid


def random_connect_node_grid(grid, min_connections, max_connections):
    columns = len(grid)
    rows = len(grid[0])

    # Connect the nodes
    for x in range(0, columns):
        for y in range(0, rows):
            num = random.randint(min_connections, max_connections)
            directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1, 1)]
            while num > 0:
                if len(directions) > 0:
                    rand_dir = directions[random.randint(0, len(directions) - 1)]
                    contarget = (x + rand_dir[0], y + rand_dir[1])
                    if 0 <= contarget[0] < columns and 0 <= contarget[1] < rows:
                        grid[x][y].add_successor(grid[contarget[0]][contarget[1]])
                        num -= 1
                    directions.remove(rand_dir)
                else:
                    break
    # ~Connect the nodes


def two_way_connect(node1, node2):
    node1.add_successor(node2)
    node2.add_successor(node1)


def add_grid_filling_path(grid):
    columns = len(grid)
    rows = len(grid[0])

    for x in range(0, columns):
        if x < columns - 1:
            if x % 2 == 0:
                two_way_connect(grid[x][0], grid[x+1][0])
            else:
                two_way_connect(grid[x][-1], grid[x+1][-1])

        for y in range(0, rows):
            if y < (rows - 1):
                two_way_connect(grid[x][y], grid[x][y+1])



def generate_grid_graph(grid_dimensions=(1200, 800), spacing=40, origin=(0, 0), min_connections=1, max_connections=4, connected=True):
    """ Returns a list of nodes arranged in a grid pattern"""
    grid = generate_disconnected_node_grid(grid_dimensions, spacing, origin)

    if connected:
        add_grid_filling_path(grid)
        random_connect_node_grid(grid, min_connections - 1, max_connections - 1)
    else:
        random_connect_node_grid(grid, min_connections, max_connections)

    node_list = []
    for column in grid:
        node_list.extend(column)

    return node_list
