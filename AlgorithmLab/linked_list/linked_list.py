class LinkedListNode(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def delete_node(node: LinkedListNode):
    next_node = node.next
    if not next_node:
        raise Exception("The last node cannot be deleted")
    node.value = next_node.value
    node.next = next_node.next
