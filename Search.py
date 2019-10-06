

def breadth_first(start, goal):
    frontier = [[start]]
    while len(frontier) > 0:
        # select path from frontier
        path = frontier.pop(0)
        #
        if path[-1] == goal:
            return path
        else:
            for succ in path[-1].successors:
                frontier.append(path + [succ])
