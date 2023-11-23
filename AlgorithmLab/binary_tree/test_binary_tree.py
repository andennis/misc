import pytest
from typing import List
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
    (TreeNode(1, left=TreeNode(0)), [1, 0, None]),
    (TreeNode(1,
              left=TreeNode(0,
                            left=TreeNode(-3),
                            right=TreeNode(8,
                                           left=TreeNode(6))),
              right=TreeNode(5)),
     [1, 0, 5, -3, 8, None, None, None, None, 6, None]),
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
     [1, 2, 3, None,  4, 5, None]),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4)),
              right=TreeNode(3)),
     [1, 2, 3, 4, None, None, None])
])
def test_tree_to_list(root, result):
    assert TreeNodeTraversal.tree_to_level_list(root) == result


@pytest.mark.parametrize("inorder, postorder, result", [
    ([], [], []),
    ([2, 1], [2, 1], [1, 2, None]),
    ([1, 2], [2, 1], [1, None, 2]),
    ([2, 1, 3], [2, 3, 1], [1, 2, 3]),
    ([2, 1, 4, 3], [2, 4, 3, 1], [1, 2, 3, None, None, 4, None]),
    ([2, 1, 3, 4], [2, 4, 3, 1], [1, 2, 3, None, None, None, 4]),
    ([4, 2, 1, 3], [4, 2, 3, 1], [1, 2, 3, 4, None, None, None]),
    ([2, 4, 1, 3], [4, 2, 3, 1], [1, 2, 3, None, 4, None, None]),
    ([2, 1, 3, 5, 4], [2, 5, 4, 3, 1], [1, 2, 3, None, None, None, 4, 5, None]),
    ([2, 4, 5, 3, 6, 1, 7], [5, 4, 6, 3, 2, 7, 1], [1, 2, 7, None, 3, None, None, 4, 6, None, 5, None, None]),
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
    (
        [4, 11, 10, 2, 8, 6, 9, 5, 7, 1, 3, 13, 12],
        [11, 10, 4, 8, 9, 6, 7, 5, 2, 13, 12, 3, 1],
        [1, 2, 3, 4, 5, None, 12, None, 10, 6, 7, 13, None, 11, None, 8, 9, None, None, None, None]
     ),
    # (
    #     [-80,25,98,13,16,79,-59,-49,-50,-83,6,-96,85,-36,77,20,55,23,92,72,-58,-6,14,-76,-46,41,-37,17,64,88,-73,-85,-52,30,75,19,-42,-55,87,80,59,-27,-81,1,44,-14,84,-10,-60,-34,91,-87,31,42,5,-18,38,86,-25,74,22,-7,-90,56,-72,32,-24,50,-13,-71,83,60,34,-20,49,58,53,-4,-89,78,27,-21,-16,-54,67,-1,21,11,-22,81,40,-92,-29,89,-95,-48,47,-23,-3,-19,61,-99,4,48,-63,-79,-30,-100,54,-70,94,39,-9,-41,-82,15,-98,-15,-97,-43,-64,43,97,51,82,68,96,-5,36,28,35,-69,65,24,-74,57,66,-94,-88,18,37,0,29,9,76,-61,33,69,-39,3,-44,90,-65,95,-26,2,93,-78,-84,-17,-12,-66,-75,-40,99,73,-57,7,26,-68,8,12,-8,62,46,-51,-67,-47,-2,52,-77,-86,10,-38,-93,-35,45,-31,-91,63,71,-28,-53,-56,-32,-33,-45,70,-62,-11],
    #     [-80,98,25,13,79,-49,-59,6,-83,-96,-36,85,-50,20,23,92,55,72,-6,-76,14,41,64,17,-73,-85,30,-52,75,88,-37,87,59,-27,80,1,-81,-55,44,-42,-14,19,-46,-60,-34,-87,31,91,-10,-18,38,-25,74,86,5,42,-90,-7,22,-72,32,56,50,-71,-13,-24,60,-20,34,58,-4,78,-16,-21,-54,27,-89,53,49,83,-1,21,81,40,-29,89,-92,-22,11,47,-23,-19,-3,-48,-99,61,-95,48,-79,-100,54,-70,39,-9,-82,-41,94,-30,15,-63,-15,-97,43,97,-64,51,-43,-98,4,67,84,82,-58,77,16,96,36,35,-69,65,28,-5,-74,57,18,-88,0,37,-94,66,24,9,-61,76,29,3,-39,90,-65,-44,2,-26,95,69,-17,-84,-78,93,-66,-40,99,-57,-68,26,7,73,46,62,-8,12,-47,-67,-2,-51,-86,10,45,-35,-93,-38,-31,-77,63,71,-91,-28,-56,-33,-32,70,-11,-62,-45,-53,52,8,-75,-12,33,68],
    #     [68,16,33,13,77,29,-12,25,None,-50,-58,24,76,93,-75,-80,98,-59,85,72,82,-5,66,9,-61,69,-78,-66,8,None,None,None,None,79,-49,-96,-36,55,None,84,None,96,28,57,-94,None,None,None,None,None,95,None,-84,None,None,73,52,None,None,None,None,-83,None,None,None,20,92,-46,67,None,None,36,65,-74,None,None,37,-44,-26,None,-17,99,7,-51,-53,None,6,None,None,23,None,14,19,83,4,None,None,-69,None,None,None,-88,0,-39,-65,None,2,None,None,-40,None,-57,26,12,-2,-28,-45,None,None,None,None,-6,-76,-37,-14,-24,49,-95,-98,35,None,None,18,None,None,None,3,90,None,None,None,None,None,None,None,None,-68,None,-8,-67,None,-91,None,-32,-62,None,None,None,None,41,88,-42,None,56,-13,34,53,11,61,-63,-43,None,None,None,None,None,None,None,None,None,None,None,62,None,-47,-77,71,-56,-33,70,-11,None,None,17,75,None,44,22,32,50,-71,60,-20,58,-89,21,-22,-48,-99,48,15,-97,51,None,46,None,None,None,-31,63,None,None,None,None,None,None,None,None,None,None,64,-52,None,-55,None,42,-7,-72,None,None,None,None,None,None,None,None,None,None,None,-4,27,-1,None,None,-92,None,-3,None,None,None,None,-30,None,-15,None,-64,None,None,None,-38,None,None,None,None,None,-85,30,None,-81,-10,5,None,-90,None,None,None,None,78,-54,None,None,40,89,-23,-19,-79,94,None,None,None,97,10,-93,-73,None,None,None,80,1,None,91,None,86,None,None,None,None,-21,None,81,None,-29,None,47,None,None,None,None,None,-70,-41,43,None,-86,None,None,-35,None,None,87,-27,None,None,-34,31,38,74,None,-16,None,None,None,None,None,None,54,None,-9,-82,None,None,None,None,None,45,None,None,59,None,-60,None,-87,None,-18,None,-25,None,None,None,-100,None,39]
    # )
])
def test_build_tree_using_inorder_and_preorder(inorder: List[int], postorder: List[int], result: List[int]):
    node = TreeNodeTraversal().build_tree_inorder_postorder_iteratively(inorder, postorder)
    assert TreeNodeTraversal.tree_to_level_list(node) == result

    node = TreeNodeTraversal().build_tree_inorder_postorder_recursively_v1(inorder, postorder)
    assert TreeNodeTraversal.tree_to_level_list(node) == result

    node = TreeNodeTraversal.build_tree_inorder_postorder_recursively_v2(inorder, postorder)
    assert TreeNodeTraversal.tree_to_level_list(node) == result


