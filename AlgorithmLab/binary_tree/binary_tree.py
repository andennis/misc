from typing import Optional, List
from collections import Counter

from binary_tree import TreeNode


class TreeNodeTraversal:
    def __init__(self):
        self.nodes = []
        self.inorder_nodes = []
        self.inorder = []
        self.postorder = []

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
        self._get_level_node_values(root, 0, node_values)
        return node_values

    @classmethod
    def _get_level_node_values(cls, root: Optional[TreeNode], level: int, node_vals: List[List[int]]):
        if not root:
            return
        if level >= len(node_vals):
            node_vals.append([])
        node_vals[level].append(root.val)

        cls._get_level_node_values(root.left, level + 1, node_vals)
        cls._get_level_node_values(root.right, level + 1, node_vals)

    @staticmethod
    def level_order_traversal_iteratively(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = [root]
        level = 0
        nodes_vals = []
        while nodes:
            level_nodes_num = len(nodes)
            nodes_vals.append([])
            for _ in range(level_nodes_num):
                node = nodes.pop(0)
                nodes_vals[level].append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            level += 1

        return nodes_vals

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1

    def is_symmetric_iteratively(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        nodes = [root]
        while nodes:
            level_nodes_num = len(nodes)
            for i in range(level_nodes_num // 2):
                left_val = nodes[i].val if nodes[i] else None
                right_val = nodes[-(i+1)].val if nodes[-(i+1)] else None
                if left_val != right_val:
                    return False

            for i in range(level_nodes_num):
                node = nodes.pop(0)
                if node:
                    nodes.append(node.left)
                    nodes.append(node.right)

        return True

    def is_symmetric_recursively(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        levels = []
        self._get_symmetric_level_nodes(root, 0, levels)
        for nodes in levels:
            for i in range(len(nodes) // 2):
                left_val = nodes[i].val if nodes[i] else None
                right_val = nodes[-(i+1)].val if nodes[-(i+1)] else None
                if left_val != right_val:
                    return False
        return True

    def _get_symmetric_level_nodes(self, root: Optional[TreeNode], level, nodes):
        if not root:
            return
        if level >= len(nodes):
            nodes.append([])

        nodes[level].extend([root.left, root.right])
        self._get_symmetric_level_nodes(root.left, level + 1, nodes)
        self._get_symmetric_level_nodes(root.right, level + 1, nodes)

    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        return self._calc_path(root, target_sum, 0)

    def _calc_path(self, root: Optional[TreeNode], target_sum, cur_sum) -> bool:
        if not root:
            return False

        cur_sum += root.val
        if root.left is None and root.right is None:
            return cur_sum == target_sum

        if self._calc_path(root.left, target_sum, cur_sum):
            return True
        return self._calc_path(root.right, target_sum, cur_sum)

    @staticmethod
    def count_unival_subtrees_v1(root: Optional[TreeNode]) -> int:
        def is_unival_subtrees(node: Optional[TreeNode]):
            if not node:
                return True
            if not (node.left or node.right):
                return True

            global count
            is_left = is_unival_subtrees(node.left)
            if is_left and node.left:
                count += 1
            is_right = is_unival_subtrees(node.right)
            if is_right and node.right:
                count += 1

            is_left = node.val == (node.left.val if node.left else node.val) and is_left
            is_right = node.val == (node.right.val if node.right else node.val) and is_right
            return is_left and is_right

        if not root:
            return 0

        global count
        count = 0
        if is_unival_subtrees(root):
            count += 1
        return count

    def count_unival_subtrees_v2(self, root: Optional[TreeNode]) -> int:
        def count_subtrees(node: Optional[TreeNode]):
            if not node:
                return True

            is_left = count_subtrees(node.left)
            is_right = count_subtrees(node.right)
            if is_left and is_right:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                self.count += 1
                return True

            return False

        if not root:
            return 0

        self.count = 0
        count_subtrees(root)
        return self.count
