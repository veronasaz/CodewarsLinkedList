class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s: str) -> Node:
    if not s or s in ["null", "NULL", "nil", "nullptr", "null()", "None"]:
        return None

    values = s.split(" -> ")

    head = Node(int(values[0]))

    current = head
    for value in values[1:]:
        if value in ["null", "NULL", "nil", "nullptr", "null()", "None"]:
            break
        current.next = Node(int(value))
        current = current.next

    return head
