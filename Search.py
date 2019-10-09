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


def generic_search(start, goal, path_select_func, log=False):
        """ path_select_func should be a function that selects a path from 
         frontier to expand, removes it from the frontier and returns it """
        frontier = [[start]]
        iterations = 0
        while len(frontier) > 0:
                if log:
                        print("itration " + str(iterations) + "    frontier: " + frontier_string(frontier))
                path = path_select_func(frontier)        
                if path[-1] == goal:
                    return path
                else:
                    for succ in path[-1].successors:
                        frontier.append(path + [succ])
                iterations += 1



def breadth_first(start, goal):
        def select_first(frontier):
                return frontier.pop(0)
        return generic_search(start, goal, select_first)



def depth_first(start, goal):
        def select_last(frontier):
                return frontier.pop(-1)
        return generic_search(start, goal, select_last)
