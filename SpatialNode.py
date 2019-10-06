from Node import Node

class SpatialNode(Node):
    def __init__(self, position):
        super(SpatialNode, self).__init__()
        self.position = position