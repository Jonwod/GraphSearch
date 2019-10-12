class Node(object):
    def __init__(self, successors=[]):
        self.__successors = list(successors)
        self.id = Node.id_counter
        Node.id_counter += 1
    id_counter = 0

    @property
    def successors(self):
        return self.__successors

    def add_successor(self, new_successor):
        if new_successor not in self.__successors:
            self.__successors.append(new_successor)
