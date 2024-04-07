class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if not node:
        raise ValueError("node is None")
    if index < 0:
        raise ValueError("index cannot be less than 0")
    while index > 0:
        node = node.next
        index -= 1
        if not node:
            raise ValueError("index is out of bounds")
    return node
