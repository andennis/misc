from typing import Optional


# Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.
class ListNode(object):

    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node


def delete_node(node: ListNode):
    next_node = node.next
    if not next_node:
        raise Exception("The last node cannot be deleted")
    node.val = next_node.val
    node.next = next_node.next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    def nodes_count(node: Optional[ListNode], node_index: int) -> tuple[Optional[ListNode], int]:
        if not node:
            return None, node_index

        next_node, count = nodes_count(node.next, node_index + 1)
        if not next_node and node_index == count // 2:
            return node, node_index

        return next_node, count

    result = nodes_count(head, 0)
    return result[0]
