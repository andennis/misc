import pytest
from binary_tree import TreeNodeTraversal, TreeNode


@pytest.mark.parametrize("root, result", [
    (None, []),
    (TreeNode(1), [1]),
    (TreeNode(1, left=TreeNode(2)), [1, 2]),
    (TreeNode(1, left=None, right=TreeNode(3)), [1, 3]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3,
                             left=TreeNode(4),
                             right=TreeNode(5)
                             )
              ),
     [1, 2, 3, 4, 5]),
    (TreeNode(1, left=None, right=TreeNode(3, left=TreeNode(4))), [1, 3, 4]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4,
                                          left=TreeNode(8,
                                                        right=TreeNode(12,
                                                                       left=TreeNode(16),
                                                                       right=TreeNode(17)))),
                            right=TreeNode(5,
                                           right=TreeNode(9,
                                                          left=TreeNode(13)))),
              right=TreeNode(3,
                             left=TreeNode(6,
                                           right=TreeNode(10,
                                                          left=TreeNode(14))),
                             right=TreeNode(7,
                                            left=TreeNode(11,
                                                          right=TreeNode(15)
                                                          )
                                            )
                             )
              ),
     [1, 2, 4, 8, 12, 16, 17, 5, 9, 13, 3, 6, 10, 14, 7, 11, 15])
])
def test_preorder_traversal(root, result):
    assert TreeNodeTraversal().preorder_traversal(root) == result
