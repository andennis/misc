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


def reverse_between(head: ListNode, m: int, n: int) -> Optional[ListNode]:
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    # Empty list
    if not head:
        return None

    # Move the two pointers until they reach the proper starting point
    # in the list.
    cur, prev = head, None
    while m > 1:
        prev = cur
        cur = cur.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail, con = cur, prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        n -= 1

    # Adjust the final connections as explained in the algorithm
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head