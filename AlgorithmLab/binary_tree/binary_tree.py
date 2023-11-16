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
            cur_node = self.nodes[i - 1]

            # The left traversed nodes can be removed as right traversal is going to be performed
            if cur_node == root and self._can_right_node_be_traversed(cur_node):
                self.nodes = [root] + [root.left] if root.left else []

        if root not in self.inorder_nodes:
            self.inorder_nodes.append(root)

        return [v.val for v in self.inorder_nodes]

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
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
            if self._can_right_node_be_traversed(cur_node):
                cur_node = cur_node.right
                self.nodes.append(cur_node)
                continue

            if cur_node not in self.inorder_nodes:
                self.inorder_nodes.append(cur_node)

            i = len(self.nodes) - 1 - self.nodes[::-1].index(cur_node)
            cur_node = self.nodes[i - 1]

            # The left traversed nodes can be removed as right traversal is going to be performed
            if cur_node == root and self._can_right_node_be_traversed(cur_node):
                self.nodes = [root] + [root.left] if root.left else []

        # The 'while' circle above does not add root node. So, it must be added here
        self.inorder_nodes.append(root)

        return [v.val for v in self.inorder_nodes]

    def _can_left_node_be_traversed(self, node: TreeNode):
        return node.left is not None and node.left not in self.nodes

    def _can_right_node_be_traversed(self, node: TreeNode):
        return node.right is not None and node.right not in self.nodes

    def level_order_traversal_recursively(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_values = []
        self._get_level_nodes(root, 0, node_values)
        return node_values

    @classmethod
    def _get_level_nodes(cls, root: Optional[TreeNode], level: int, node_vals: List[List[int]]):
        if not root:
            return
        if level >= len(node_vals):
            node_vals.append([])
        node_vals[level].append(root.val)

        cls._get_level_nodes(root.left, level + 1, node_vals)
        cls._get_level_nodes(root.right, level + 1, node_vals)

    @staticmethod
    def level_order_traversal_by_queue(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = [root]
        level = 0
        nodes_vals = []
        while nodes:
            level_nodes_num = len(nodes)
            nodes_vals.append([])
            for i in range(level_nodes_num):
                node = nodes.pop(0)
                nodes_vals[level].append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            level += 1

        return nodes_vals
