import random
from SpatialNode import SpatialNode

# def generate_spatial_tree(min_branching_factor, max_branching_factor, max_depth):
#     current_depth = 0
#     base_node = SpatialNode((0, 0))
#     nodes = [base_node]
#     frontier = [base_node]
#     spacing = 40
#
#     while current_depth < max_depth:
#         next_frontier = []
#         for node in frontier:
#             branches = random.randint(min_branching_factor, max_branching_factor)
#             for i in range(0, branches):
#                 new_node = Node()
#                 node.successors.append(new_node)
#                 next_frontier.append(new_node)
#                 nodes.append(new_node)
#         current_depth += 1
#         frontier = next_frontier
#     return nodes


def generate_grid_graph(grid_dimensions=(1200, 800), spacing=40, origin=(0, 0), min_connections=1, max_connections=4):
    """ Returns a list of nodes arranged in a grid pattern"""
    columns = int(grid_dimensions[0]) // spacing
    rows = int(grid_dimensions[1]) // spacing
    grid = []
    for x in range(0, columns):
        # Add column
        grid.append([])
        for y in range(0, rows):
            pos = (origin[0] + x*spacing, origin[1] + y*spacing)
            grid[x].append(SpatialNode(pos))

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
                        grid[x][y].successors.append(grid[contarget[0]][contarget[1]])
                        num -= 1
                    directions.remove(rand_dir)
                else:
                    break
    # ~Connect the nodes

    node_list = []
    for column in grid:
        node_list.extend(column)

    return node_list



def generate_spatial_tree(min_branch, max_branch, depth, origin=(0, 0), horizontal_spacing = 30, vertical_spacing = 100):
    base_width = horizontal_spacing * max_branch ** depth
    def expand_node(node, node_list, branches, current_depth):
        for i in range(0, branches):

            new_node = SpatialNode(origin)
            node_list.append(new_node)
            node.successors.append(new_node)
            if d > 1:
                expand_node(new_node, node_list, random.randint(min_branch, max_branch), d - 1)


    node_list = [SpatialNode(origin)]
    expand_node(node_list[0], node_list, random.randint(min_branch, max_branch), 1)



