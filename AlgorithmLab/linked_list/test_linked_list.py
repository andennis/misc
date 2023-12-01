import pytest
from linked_list import delete_node, ListNode, middle_node


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
