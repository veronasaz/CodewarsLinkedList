class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head: Node, data: int) -> Node:
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
