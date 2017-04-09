from linked_list import sList
from node import Node

def main():

    # initialize the list and nodes
    ll = sList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    # create a linked list with 3 nodes
    ll.push_back(node1)
    ll.push_back(node2)
    ll.push_back(node3)

    # test the class functionality
    # get_size
    assert ll.get_size() == 3

    # is_empty
    assert ll.is_empty() == False

    # value_at
    assert ll.value_at(0) == 1
    # assert ll.value_at(10) == None

    # push_front
    ll.push_front(node4)
    assert ll.get_size() == 4
    assert ll.value_at(0) == 4

    # pop_front
    x = ll.pop_front()
    assert x == 4
    assert ll.get_size() == 3
    assert ll.value_at(0) == 1

    # push_back
    ll.push_back(node5)
    assert ll.get_size() == 4
    assert ll.value_at(3) == 5

    # pop_back
    x = ll.pop_back()
    assert x == 5
    assert ll.get_size() == 3
    assert ll.value_at(2) == 3

    # front and back
    assert ll.front() == 1
    assert ll.back() == 3

    # insert
    ll.insert(0, node6)
    assert ll.front() == 6
    assert ll.get_size() == 4

    # erase
    ll.erase(0)
    assert ll.front() == 1
    assert ll.get_size() == 3

    # value_n_from_end
    assert ll.value_n_from_end(1) == 3

    # reverse
    ll.reverse()
    assert ll.front() == 3
    assert ll.back() == 1
    assert ll.get_size() == 3

    # remove_value
    ll.remove_value(3)
    assert ll.front() == 2

if __name__ == "__main__":
    main()

















































