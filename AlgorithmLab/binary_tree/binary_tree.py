from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeTraversal:
    def __init__(self):
        self.nodes = None

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.nodes = [root]
        cur_node = root
        while cur_node != root \
                or self._is_left_node_traversed(cur_node) \
                or self._is_right_node_traversed(cur_node):
            if self._is_left_node_traversed(cur_node):
                self.nodes.append(cur_node.left)
                cur_node = cur_node.left
                continue

            if self._is_right_node_traversed(cur_node):
                self.nodes.append(cur_node.right)
                cur_node = cur_node.right
                continue

            i = len(self.nodes) - 1 - self.nodes[::-1].index(cur_node) - 1
            cur_node = self.nodes[i]

        return [v.val for v in self.nodes]

    def _is_left_node_traversed(self, node: TreeNode):
        return node.left is not None and node.left not in self.nodes

    def _is_right_node_traversed(self, node: TreeNode):
        return node.right is not None and node.right not in self.nodes
