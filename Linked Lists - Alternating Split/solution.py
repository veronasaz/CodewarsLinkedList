class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head: Node) -> Context:
    if head is None or head.next is None:
        raise ValueError('head must have at least two nodes')
    
    first = head
    second = head.next
    first_head = first
    second_head = second
    
    while first is not None and second is not None:
        first.next = second.next
        first = first.next
        if first is not None:
            second.next = first.next
            second = second.next
    
    return Context(first_head, second_head)
