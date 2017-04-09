class Node(object):

    "node class"

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return "The value of this node is: {}".format(self.value)

