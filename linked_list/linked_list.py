from node import Node

class sList(object):

    "No tail pointer"
    def __init__(self, head = None):
        self.head = head
        if head:
        #     "initailize with a list of nodes"
        #     tmp = self.head
        #     self.size = 1
        #     while tmp.next != None:
        #         tmp = tmp.next
        #         self.size += 1
        # else:
        #     "initialize without nodes"
            self.size = 1
        else:
            self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def value_at(self, n):
        if n < self.size:
            tmp = self.head
            for i in range(n):
                tmp = tmp.next
            return tmp.value

    def push_front(self, item):
        if self.size == 0:
            self.head = item
        else:
            item.next = self.head
            self.head = item
        self.size += 1

    def pop_front(self):
        if self.size > 0:
            tmp = self.head
            self.head = self.head.next
            self.size -= 1
            return tmp.value

    def push_back(self,item):
        if self.size == 0:
            self.head = item
            self.size += 1
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = item
            self.size += 1

    def pop_back(self):
        if self.size == 1:
            tmp = self.head
            self.head = None
            self.size -= 1
            return tmp.value
        elif self.size > 1:
            tmp = self.head
            while tmp.next.next != None:
                tmp = tmp.next
            last_node = tmp.next
            tmp.next = last_node.next
            self.size -= 1
            return last_node.value

    def front(self):
        if self.size > 0:
            return self.head.value

    def back(self):
        if self.size > 0:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            return tmp.value

    def insert(self, index, item):
        if index < self.size:
            tmp = self.head
            if index == 0:
                self.push_front(item)
            else:
                for i in range(index-1):
                    tmp = tmp.next
                item.next = tmp.next
                tmp.next = item
                self.size += 1

    def erase(self,index):
        if index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                tmp = self.head
                for i in range(index-1):
                    tmp = tmp.next
                tmp.next = tmp.next.next
            self.size -= 1

    def value_n_from_end(self,n):
        if n <= self.size:
            front = self.head
            end = self.head
            for i in range(n-1):
                end = end.next
            while end.next != None:
                end = end.next
                front = front.next
            return front.value

    def reverse(self):
        if self.size > 1:
            front = self.head
            end = self.head.next
            front.next = None
            while end != None:
                tmp = end.next
                end.next = front
                front = end
                end = tmp
            self.head = front

    def remove_value(self, value):
        if self.size > 0:
            if self.head.value == value:
                self.head = self.head.next
                self.size -= 1
            else:
                if self.size > 1:
                    front = self.head
                    end = self.head.next
                    while (end.next != None) and (end.value != value):
                        front = end
                        end = end.next
                    if end.value == value:
                        front.next = end.next
                    self.size -= 1



















