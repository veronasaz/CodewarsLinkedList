class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head: Node) -> Node:
    node = Node()
    node.next = head
    prev = node
    while head and head.next:
        first = head
        second = head.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        head = first.next
    return node.next
