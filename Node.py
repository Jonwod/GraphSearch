class Node(object):
    def __init__(self, successors=[]):
        self.successors = list(successors)
        self.id = Node.id_counter
        Node.id_counter += 1
    id_counter = 0
