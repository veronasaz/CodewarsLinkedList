class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    def reverse_recursive(current: Node, prev: Node) -> Node:
        if current is None:
            return prev
        
        next_node = current.next
        current.next = prev
        return reverse_recursive(next_node, current)
    
    return reverse_recursive(head, None)
