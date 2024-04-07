class Node():
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

def stringify(node: Node) -> str:
    '''
    Convert a linked list to a string.
    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    '0 -> 1 -> 4 -> 9 -> 16 -> None'
    >>> stringify(None)
    'None'
    '''
    res = ''
    if node is None:
        return 'None'
    else:
        probe = node
        while probe is not None:
            res += f"{probe.data} -> "
            probe = probe.next
        return res + 'None'

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
