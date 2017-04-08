class node(object):

    "node class"

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def __str__(self):
        return "The value of this node is: {}".format(self.value)

