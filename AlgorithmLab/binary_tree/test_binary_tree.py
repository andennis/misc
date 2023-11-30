import pytest

from binary_tree import TreeNode, BinaryTreeTraversal
from .binary_tree import TreeNodeTraversal


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


@pytest.mark.parametrize("root, result", [
    (None, []),
    (TreeNode(1), [1]),
    (TreeNode(1, left=TreeNode(2)), [2, 1]),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), [2, 1, 3]),
    (TreeNode(1, left=None, right=TreeNode(3)), [1, 3]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3,
                             left=TreeNode(4),
                             right=TreeNode(5)
                             )
              ),
     [2, 1, 4, 3, 5]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)),
              right=TreeNode(5)
              ),
     [3, 2, 4, 1, 5]),
    (TreeNode(1, left=None, right=TreeNode(3, left=TreeNode(4))), [1, 4, 3]),
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
     [8, 16, 12, 17, 4, 2, 5, 13, 9, 1, 6, 14, 10, 3, 11, 15, 7])
])
def test_inorder_traversal(root, result):
    assert TreeNodeTraversal().inorder_traversal(root) == result


@pytest.mark.parametrize("root, result", [
    (None, []),
    (TreeNode(1), [1]),
    (TreeNode(1, left=TreeNode(2)), [2, 1]),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), [2, 3, 1]),
    (TreeNode(1, left=None, right=TreeNode(3)), [3, 1]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3,
                             left=TreeNode(4),
                             right=TreeNode(5)
                             )
              ),
     [2, 4, 5, 3, 1]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)),
              right=TreeNode(5)
              ),
     [3, 4, 2, 5, 1]),
    (TreeNode(1, left=None, right=TreeNode(3, left=TreeNode(4))), [4, 3, 1]),
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
     [16, 17, 12, 8, 4, 13, 9, 5, 2, 14, 10, 6, 15, 11, 7, 3, 1])
])
def test_postorder_traversal(root, result):
    assert TreeNodeTraversal().postorder_traversal(root) == result


@pytest.mark.parametrize("root, result", [
    (None, []),
    (TreeNode(1), [[1]]),
    (TreeNode(1, left=TreeNode(2)), [[1], [2]]),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), [[1], [2, 3]]),
    (TreeNode(1, left=None, right=TreeNode(3)), [[1], [3]]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3,
                             left=TreeNode(4),
                             right=TreeNode(5)
                             )
              ),
     [[1], [2, 3], [4, 5]]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)),
              right=TreeNode(5)
              ),
     [[1], [2, 5], [3, 4]]),
    (TreeNode(1, left=None, right=TreeNode(3, left=TreeNode(4))), [[1], [3], [4]]),
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
     [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17]])
])
def test_level_order_traversal_recursively(root, result):
    assert TreeNodeTraversal().level_order_traversal_recursively(root) == result
    assert TreeNodeTraversal.level_order_traversal_iteratively(root) == result


@pytest.mark.parametrize("root, result", [
    (None, 0),
    (TreeNode(1), 1),
    (TreeNode(1, left=TreeNode(2)), 2),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), 2),
    (TreeNode(1, left=None, right=TreeNode(3)), 2),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3,
                             left=TreeNode(4),
                             right=TreeNode(5)
                             )
              ),
     3),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)),
              right=TreeNode(5)
              ),
     3),
    (TreeNode(1,
              left=None,
              right=TreeNode(3,
                             left=TreeNode(4))),
     3),
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
     6)
])
def test_max_depth(root, result):
    assert TreeNodeTraversal().max_depth(root) == result


@pytest.mark.parametrize("root, result", [
    (None, False),
    (TreeNode(1), True),
    (TreeNode(1, left=TreeNode(0)), False),
    (TreeNode(1, left=TreeNode(2)), False),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(2)
              ),
     True),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)
              ),
     False),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)
                            ),
              right=TreeNode(2,
                             left=TreeNode(4),
                             right=TreeNode(3)
                             )
              ),
     True),
    (TreeNode(1,
              left=TreeNode(2,
                            right=TreeNode(3)
                            ),
              right=TreeNode(2,
                             right=TreeNode(3)
                             )
              ),
     False)
])
def test_is_symmetric(root, result):
    assert TreeNodeTraversal().is_symmetric_iteratively(root) == result
    assert TreeNodeTraversal().is_symmetric_recursively(root) == result


@pytest.mark.parametrize("root, target_sum, result", [
    (None, 1, False),
    (TreeNode(1), 2, False),
    (TreeNode(1), 1, True),
    (TreeNode(1, left=TreeNode(0)), 1, True),
    (TreeNode(1, left=TreeNode(2)), 1, False),
    (TreeNode(-2, right=TreeNode(-3)), -5, True),
    (TreeNode(-2, right=TreeNode(-3, left=TreeNode(5))), 0, True),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)
              ),
     4, True),
    (TreeNode(1,
              right=TreeNode(6,
                             left=TreeNode(4))
              ),
     8, False),
    (TreeNode(1,
              right=TreeNode(6,
                             left=TreeNode(4))
              ),
     7, False),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(3),
                            right=TreeNode(4)
                            ),
              right=TreeNode(2,
                             right=TreeNode(7)
                             )
              ),
     10, True)
])
def test_has_path_sum(root, target_sum, result):
    assert TreeNodeTraversal().has_path_sum(root, target_sum) == result


@pytest.mark.parametrize("root, result", [
    (None, []),
    (TreeNode(1), [1]),
    (TreeNode(1, left=TreeNode(0)), [1, 0]),
    (TreeNode(1,
              left=TreeNode(0,
                            left=TreeNode(-3),
                            right=TreeNode(8,
                                           left=TreeNode(6))),
              right=TreeNode(5)),
     [1, 0, 5, -3, 8, None, None, None, None, 6]),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)
              ),
     [1, 2, 3]),
    (TreeNode(1,
              left=TreeNode(2,
                            right=TreeNode(4)
                            ),
              right=TreeNode(3,
                             left=TreeNode(5)
                             )
              ),
     [1, 2, 3, None,  4, 5]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4)),
              right=TreeNode(3)),
     [1, 2, 3, 4])
])
def test_tree_to_list(root, result):
    assert BinaryTreeTraversal.tree_to_level_list(root) == result


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
    # assert TreeNodeTraversal.count_unival_subtrees_v1(root) == result
    # assert TreeNodeTraversal().count_unival_subtrees_v2(root) == result
    assert TreeNodeTraversal.count_unival_subtrees_v3(root) == result
