import pytest
from linked_list import delete_node, LinkedListNode


def test_delete_first_node():
    c = LinkedListNode('C')
    b = LinkedListNode('B', c)
    a = LinkedListNode('A', b)
    delete_node(a)
    assert a.value == 'B'
    assert a.next.value == 'C'


def test_delete_middle_node():
    c = LinkedListNode('C')
    b = LinkedListNode('B', c)
    a = LinkedListNode('A', b)

    delete_node(b)
    assert a.next.value == 'C'


def test_delete_last_node():
    b = LinkedListNode('B')
    a = LinkedListNode('A', b)
    with pytest.raises(Exception):
        delete_node(b)
