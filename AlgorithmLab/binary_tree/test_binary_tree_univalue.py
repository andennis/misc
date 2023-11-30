import pytest

from binary_tree import TreeNode
from binary_tree.binary_tree_univalue import BinaryTreeUnivalue


@pytest.mark.parametrize("root, result", [
    (None, 0),
    (TreeNode(1), 1),
    (TreeNode(1,
              right=TreeNode(2)),
     1),
    (TreeNode(1,
              right=TreeNode(1)),
     2),
    (TreeNode(1,
              left=TreeNode(1)),
     2),
    (TreeNode(1,
              left=TreeNode(1),
              right=TreeNode(1)),
     3),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(1)),
     2),
    (TreeNode(1,
              left=TreeNode(1),
              right=TreeNode(2)),
     2),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)),
     2),
    (TreeNode(1,
              left=TreeNode(0),
              right=TreeNode(0)),
     2),
    (TreeNode(1,
              left=TreeNode(1,
                            left=TreeNode(0),
                            right=TreeNode(0)),
              right=TreeNode(0,
                             right=TreeNode(0))
              ),
     4),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3,
                                          left=TreeNode(3),
                                          right=TreeNode(3)),
                            right=TreeNode(4,
                                           left=TreeNode(4),
                                           right=TreeNode(4,
                                                          left=TreeNode(6)
                                                          )
                                           )
                            ),
              right=TreeNode(1,
                             right=TreeNode(1)
                             )
              ),
     7),
])
def test_count_unival_subtrees(root, result):
    assert BinaryTreeUnivalue.count_unival_subtrees_v1(root) == result
    assert BinaryTreeUnivalue().count_unival_subtrees_v2(root) == result
    assert BinaryTreeUnivalue.count_unival_subtrees_v3(root) == result
