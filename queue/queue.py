import sys
sys.path.insert(0, '/home/peiran/repo/Practice-Python/linked_list')

from node import Node
from linked_list import sList

class queue(object):

    def __init__(self, value = None):
        if value:
            self.qList = sList()
            qNode = Node(value = value)
            self.qList.push_back(qNode)
        else:
            self.qList = sList()

    def enqueue(self, value):
        qNode = Node(value=value)
        self.qList.push_back(qNode)

    def dequeue(self):
        if self.qList.is_empty():
            print("The queue is empty")
        else:
            self.qList.pop_front()

    def __str__(self):
        size = self.qList.get_size()
        l = []
        for i in range(size):
            l.append(self.qList.value_at(i))
        return "".join(str(l))

