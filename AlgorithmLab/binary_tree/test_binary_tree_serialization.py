import pytest
from binary_tree import TreeNode, BinaryTreeTraversal
from binary_tree.binary_tree_serialization import BinaryTreeSerialization


@pytest.mark.parametrize("root, result", [
    (None, ""),
    (TreeNode(1), "1"),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)
              ),
     "1(2,3)"),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4)
                            ),
              right=TreeNode(3,
                             right=TreeNode(-5,
                                            left=TreeNode(0),
                                            right=TreeNode(-16))
                             )
              ),
     "1(2(4),3(,-5(0,-16)))"),
])
def test_serialize_v1(root, result):
    assert BinaryTreeSerialization().serialize_v1(root) == result


@pytest.mark.parametrize("tree_data, result", [
    ("1(2(4),3(,-5(0,-16)))", [1, 2, 3, 4, None, None, -5, None, None, 0, -16])
])
def test_deserialize_v1(tree_data, result):
    root = BinaryTreeSerialization().deserialize_v1(tree_data)
    assert BinaryTreeTraversal.tree_to_level_list(root) == result


@pytest.mark.parametrize("root, result", [
    (None, ""),
    (TreeNode(1), "1:::1"),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(3)
              ),
     "1,2,3:::2,1,3"),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4),
                            right=TreeNode(6,
                                           right=TreeNode(7,
                                                          left=TreeNode(8)))
                            ),
              right=TreeNode(3,
                             right=TreeNode(-5,
                                            left=TreeNode(0),
                                            right=TreeNode(-16))
                             )
              ),
     "1,2,4,6,7,8,3,-5,0,-16:::4,2,6,8,7,1,3,0,-5,-16"),
])
def test_serialize_v2(root, result):
    assert BinaryTreeSerialization().serialize_v2(root) == result


@pytest.mark.parametrize("tree_data, result", [
    ("", []),
    ("1,2,3,4,5,6", []),
    ("1,2,3,4,5,6:::", []),
    # ("1,2,2:::2,1,2", [1, 2, 2]),
    ("1,2,3,4,5,6:::3,2,1,5,4,6", [1, 2, 4, 3, None, 5, 6]),
    ("1,2,4,3,-5,0,-16:::4,2,1,3,0,-5,-16", [1, 2, 3, 4, None, None, -5, None, None, 0, -16])
])
def test_deserialize_v2(tree_data, result):
    root = BinaryTreeSerialization().deserialize_v2(tree_data)
    assert BinaryTreeTraversal.tree_to_level_list(root) == result


@pytest.mark.parametrize("root, result", [
    (None, ","),
    (TreeNode(1), "1,,,"),
    (TreeNode(1,
              left=TreeNode(2),
              right=TreeNode(2)
              ),
     "1,2,,,2,,,"),
    (TreeNode(1,
              left=TreeNode(2,
                            left=TreeNode(4),
                            right=TreeNode(6,
                                           right=TreeNode(7,
                                                          left=TreeNode(8)))
                            ),
              right=TreeNode(3,
                             right=TreeNode(-5,
                                            left=TreeNode(0),
                                            right=TreeNode(-16))
                             )
              ),
     "1,2,4,,,6,,7,8,,,,3,,-5,0,,,-16,,,"),
])
def test_serialize_v3(root, result):
    assert BinaryTreeSerialization().serialize_v3(root) == result


@pytest.mark.parametrize("tree_data, result", [
    ("", []),
    (",", []),
    ("1,2,,,2,,,", [1, 2, 2]),
    ("1,2,4,,,6,,7,8,,,,3,,-5,0,,,-16,,,", [1, 2, 3, 4, 6, None, -5, None, None, None, 7, 0, -16, 8])
])
def test_deserialize_v3(tree_data, result):
    root = BinaryTreeSerialization().deserialize_v3(tree_data)
    assert BinaryTreeTraversal.tree_to_level_list(root) == result
