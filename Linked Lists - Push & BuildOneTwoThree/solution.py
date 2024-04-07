class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    return head
