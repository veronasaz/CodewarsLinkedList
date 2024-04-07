class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("source cannot be empty")

    new_source = source.next

    source.next = dest
    new_dest = source

    return Context(new_source, new_dest)
