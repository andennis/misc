import pytest
from typing import Optional, List

from binary_tree import TreeNode
from binary_tree.binary_tree_connect import BinaryTreeConnect


@pytest.mark.parametrize('root, result', [
    (None, []),
    (TreeNode(1), [1, None]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)), [1, None, 2, 3, None]),
    (TreeNode(1,
              left=TreeNode(2),
              ), [1, None, 2, None]),
    (TreeNode(1,
              right=TreeNode(3),
              ), [1, None, 3, None]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4,
                                          left=TreeNode(8),
                                          right=TreeNode(9)
                                          ),
                            right=TreeNode(5,
                                           left=TreeNode(10),
                                           right=TreeNode(11)
                                           )
                            ),
              right=TreeNode(3,
                             left=TreeNode(6,
                                           left=TreeNode(12),
                                           right=TreeNode(13)
                                           ),
                             right=TreeNode(7,
                                            left=TreeNode(14),
                                            right=TreeNode(15)
                                            )
                             )
              ),
     [1, None, 2, 3, None, 4, 5, 6, 7, None, 8, 9, 10, 11, 12, 13, 14, 15, None]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4),
                            right=TreeNode(5)
                            ),
              right=TreeNode(3,
                             right=TreeNode(7)
                             )
              ),
     [1, None, 2, 3, None, 4, 5, 7, None]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4,
                                          right=TreeNode(7)),
                            right=TreeNode(5,
                                           right=TreeNode(8,
                                                          left=TreeNode(10)))
                            ),
              right=TreeNode(3,
                             right=TreeNode(6,
                                            left=TreeNode(9,
                                                          right=TreeNode(11)))
                             )
              ),
     [1, None, 2, 3, None, 4, 5, 6, None, 7, 8, 9, None, 10, 11, None]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4,
                                          left=TreeNode(7)
                                          ),
                            right=TreeNode(5)),
              right=TreeNode(3,
                             right=TreeNode(6,
                                            right=TreeNode(8)
                                            )
                             )
              ),
     [1, None, 2, 3, None, 4, 5, 6, None, 7, 8, None]),
])
def test_connect_right_node(root, result):
    data = BinaryTreeConnect.connect_right_nodes_v4(root)
    assert _build_right_connection_sec(data) == result


def _build_right_connection_sec(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    nodes = [root]
    connect_seq = []
    while nodes:
        node = nodes[0]
        while node:
            connect_seq.append(node.val)
            node = node.next
        connect_seq.append(None)

        for i in range(len(nodes)):
            node = nodes.pop(0)
            if not node:
                continue
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    return connect_seq


@pytest.mark.parametrize("root, nv1, nv2, result", [
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)), 2, 3, 1),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)), 3, 1, 1),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4),
                            right=TreeNode(5)),
              right=TreeNode(3)), 4, 5, 2),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4),
                            right=TreeNode(5)),
              right=TreeNode(3)), 4, 3, 1),
    (TreeNode(3,
              left=TreeNode(5,
                            left=TreeNode(6),
                            right=TreeNode(2,
                                           left=TreeNode(7),
                                           right=TreeNode(4))),
              right=TreeNode(1,
                             left=TreeNode(0),
                             right=TreeNode(8)
                             )
              ),
     5, 1, 3),
    (TreeNode(3,
              left=TreeNode(5,
                            left=TreeNode(6),
                            right=TreeNode(2,
                                           left=TreeNode(7),
                                           right=TreeNode(4))),
              right=TreeNode(1,
                             left=TreeNode(0),
                             right=TreeNode(8)
                             )
              ),
     7, 6, 5),
    (TreeNode(3,
              left=TreeNode(5,
                            left=TreeNode(6),
                            right=TreeNode(2,
                                           left=TreeNode(7),
                                           right=TreeNode(4))),
              right=TreeNode(1,
                             left=TreeNode(0),
                             right=TreeNode(8)
                             )
              ),
     5, 4, 5),
])
def test_lowest_common_ancestor(root, nv1, nv2, result):
    nv1_node = _get_node_by_value(root, nv1)
    nv2_node = _get_node_by_value(root, nv2)
    lca_node = BinaryTreeConnect().lowest_common_ancestor(root, nv1_node, nv2_node)
    assert lca_node
    assert lca_node.val == result


def _get_node_by_value(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    l_n = _get_node_by_value(root.left, val)
    r_n = _get_node_by_value(root.right, val)
    return l_n or r_n
