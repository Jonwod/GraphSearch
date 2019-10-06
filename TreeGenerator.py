from Node import Node
import random


def generate_tree(min_branching_factor, max_branching_factor, max_depth):
    current_depth = 0
    base_node = Node()
    nodes = [base_node]
    frontier = [base_node]
    while current_depth < max_depth:
        next_frontier = []
        for node in frontier:
            branches = random.randint(min_branching_factor, max_branching_factor)
            for i in range(0, branches):
                new_node = Node()
                node.successors.append(new_node)
                next_frontier.append(new_node)
                nodes.append(new_node)
        current_depth += 1
        frontier = next_frontier
    return nodes