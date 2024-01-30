import pytest
from linked_list import delete_node, ListNode, middle_node, reverse_between


def test_delete_first_node():
    c = ListNode('C')
    b = ListNode('B', c)
    a = ListNode('A', b)
    delete_node(a)
    assert a.val == 'B'
    assert a.next.val == 'C'


def test_delete_middle_node():
    c = ListNode('C')
    b = ListNode('B', c)
    a = ListNode('A', b)

    delete_node(b)
    assert a.next.val == 'C'


def test_delete_last_node():
    b = ListNode('B')
    a = ListNode('A', b)
    with pytest.raises(Exception):
        delete_node(b)


@pytest.mark.parametrize("head, result", [
    (None, None),
    (ListNode("A"), "A"),
    (ListNode("A", ListNode("B")), "B"),
    (ListNode("A", ListNode("B", ListNode("C"))), "B"),
    (ListNode("A", ListNode("B", ListNode("C", ListNode("D")))), "C")
])
def test_middle_node(head, result):
    node = middle_node(head)
    assert node.val if node else None == result


@pytest.mark.parametrize("src_lst, left, right, result", [
    ([1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 3, 5])
])
def test_reverse_between(src_lst, left, right, result):
    head1 = _build_list(src_lst)
    head2 = _build_list(result)
    reverse_between(head1, left, right)
    assert _compare_list(head1, head2)


def _build_list(arr):
    prev = head = ListNode(arr[0])
    for v in range(1, len(arr)):
        prev.next = ListNode(v)
    return head


def _compare_list(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    if head1 or head2:
        return False

    return True
