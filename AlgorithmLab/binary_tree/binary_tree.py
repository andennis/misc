from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeTraversal:
    def __init__(self):
        self.nodes = []
        self.inorder_nodes = []

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.nodes = [root]
        cur_node = root
        while cur_node != root \
                or self._can_left_node_be_traversed(cur_node) \
                or self._can_right_node_be_traversed(cur_node):
            if self._can_left_node_be_traversed(cur_node):
                self.nodes.append(cur_node.left)
                cur_node = cur_node.left
                continue

            if self._can_right_node_be_traversed(cur_node):
                self.nodes.append(cur_node.right)
                cur_node = cur_node.right
                continue

            i = len(self.nodes) - 1 - self.nodes[::-1].index(cur_node)
            cur_node = self.nodes[i - 1]

        return [v.val for v in self.nodes]

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.nodes = [root]
        self.inorder_nodes = []
        cur_node = root
        while cur_node != root \
                or self._can_left_node_be_traversed(cur_node) \
                or self._can_right_node_be_traversed(cur_node):

            if self._can_left_node_be_traversed(cur_node):
                cur_node = cur_node.left
                self.nodes.append(cur_node)
                continue
            else:
                if cur_node not in self.inorder_nodes:
                    self.inorder_nodes.append(cur_node)
                if self._can_right_node_be_traversed(cur_node):
                    cur_node = cur_node.right
                    self.nodes.append(cur_node)
                    continue

            i = len(self.nodes) - 1 - self.nodes[::-1].index(cur_node)
            cur_node = self.nodes[i-1]

            # Remove all the traversed left nodes except the first one
            if cur_node == root and self._can_right_node_be_traversed(cur_node):
                self.nodes = [root] + [root.left] if root.left else []

        if root not in self.inorder_nodes:
            self.inorder_nodes.append(root)

        return [v.val for v in self.inorder_nodes]

    def _can_left_node_be_traversed(self, node: TreeNode):
        return node.left is not None and node.left not in self.nodes

    def _can_right_node_be_traversed(self, node: TreeNode):
        return node.right is not None and node.right not in self.nodes
