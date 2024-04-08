class Node:
    def __init__(self, next) -> None:
        self.next = next

def loop_size(node: Node) -> int:
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1

    return count
