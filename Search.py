import VecMath


def path_string(path):
    """ Path should be a list of nodes """
    string = "("
    for i in range(0, len(path)):
        node = path[i]
        if i > 0:
            string += "->"
        string += str(node.id)
    string += ")"
    return string


def frontier_string(frontier):
    """ frontier is a list of paths """
    string = "{"
    for i in range(0, len(frontier)):
        path = frontier[i]
        if i > 0:
            string += ", "
        string += path_string(path)
    string += "}"
    return string


def generic_search(start, goal, path_select_func, log=True):
    """ path_select_func should be a function that selects a path from frontier to expand, removes it from the
        frontier and returns it """
    frontier = [[start]]
    iterations = 0
    while len(frontier) > 0:
        if log:
            print("iteration " + str(iterations) + "    frontier: " + frontier_string(frontier))
        path = path_select_func(frontier)
        if path[-1] == goal:
            print("Finished in " + str(iterations) + " iterations.")
            return path
        else:
            for succ in path[-1].successors:
                frontier.append(path + [succ])
        iterations += 1


def breadth_first(start, goal):
    def select_first(frontier):
        return frontier.pop(0)

    return generic_search(start, goal, select_first)


def select_last(frontier):
    return frontier.pop(-1)


def depth_first(start, goal):
    return generic_search(start, goal, select_last)


def depth_limited_search(start, goal, depth_limit=50):
    frontier = [[start]]
    iterations = 0
    while len(frontier) > 0:
        path = select_last(frontier)
        if path[-1] == goal:
            print("Finished in " + str(iterations) + " iterations.")
            return path
        elif len(path) <= depth_limit:  # This is the bit that differs from depth_first_search
            for succ in path[-1].successors:
                frontier.append(path + [succ])
        iterations += 1


def iterative_deepening_search(start, goal):
    depth = 0
    while True:
        path = depth_limited_search(start, goal, depth)
        if path is not None:
            return path
        else:
            depth += 1


def cost_func(path):
    """ This cost function just returns the linear distance between the nodes (assumed to be spatial
            nodes)"""
    cost = 0
    for i in range(1, len(path)):
        cost += VecMath.length(VecMath.sub(path[i - 1].position, path[i].position))
    return cost


def select_lowest_cost(frontier):
    lowest_cost_path = None
    lowest_path_cost = float('inf')
    for i in range(0, len(frontier)):
        path = frontier[i]
        cost = cost_func(path)
        if cost <= lowest_path_cost:
            lowest_path_cost = cost
            lowest_cost_path = i
    return None if lowest_cost_path is None else frontier.pop(lowest_cost_path)


def uniform_cost_search(start, goal):
    return generic_search(start, goal, select_lowest_cost)


# Informed searches

def linear_distance_heuristic(path, goal):
    return VecMath.length(VecMath.sub(goal.position, path[-1].position))


def select_lowest_heuristic(frontier, goal, heuristic_func = linear_distance_heuristic):
    lowest_heuristic_path = None
    lowest_path_heuristic = float('inf')
    for i in range(0, len(frontier)):
        path = frontier[i]
        heuristic_cost = heuristic_func(path, goal)
        if heuristic_cost <= lowest_path_heuristic:
            lowest_path_heuristic = heuristic_cost
            lowest_heuristic_path = i

    return None if lowest_heuristic_path is None else frontier.pop(lowest_heuristic_path)


def greedy_search(start, goal):
    # Note that the frontier selection function is a function not just of the frontier but of the goal as well
    return generic_search(start, goal, lambda frontier: select_lowest_heuristic(frontier, goal=goal))


def a_star_heuristic(path, goal):
    return cost_func(path) + linear_distance_heuristic(path, goal)


def a_start_search(start, goal):
    return generic_search(start, goal, lambda frontier: select_lowest_heuristic(frontier, goal=goal, heuristic_func=a_star_heuristic))