from typing import Optional
from collections import deque

from binary_tree import TreeNode


class BinaryTreeConnect:

    @staticmethod
    def connect_right_nodes_v1(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes = [root]
        while nodes:
            nodes = [x for x in nodes if x is not None]
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]

            level_num = len(nodes)
            nodes2 = nodes
            nodes = [None] * level_num * 2
            for i in range(level_num):
                node = nodes2[i]
                nodes[i * 2] = node.left
                nodes[i * 2 + 1] = node.right

        return root

    @staticmethod
    def connect_right_nodes_v2(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        cur_node = root
        next_level_node = root.left or root.right
        while cur_node and next_level_node:
            if cur_node.left and cur_node.right:
                cur_node.left.next = cur_node.right

            node = cur_node.next
            while node:
                if cur_node.right:
                    cur_node.right.next = node.left or node.right
                    if cur_node.right.next:
                        break
                elif cur_node.left:
                    cur_node.left.next = node.left or node.right
                    if cur_node.left.next:
                        break
                else:
                    break
                node = node.next

            cur_node = node

            if not cur_node:
                cur_node = next_level_node
                next_level_node = next_level_node.left or next_level_node.right
                if cur_node and not next_level_node:
                    node = cur_node.next
                    while not next_level_node and node:
                        next_level_node = node.left or node.right
                        node = node.next

        return root

    @staticmethod
    def connect_right_nodes_v3(root: TreeNode) -> TreeNode:
        """Here is the best performance version from leetcode"""
        if not root:
            return root

        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()

                if i < n - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

    @staticmethod
    def connect_right_nodes_v4(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The solution from the leetcode:
            https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/editorial/
        """

        def process_child(child_node, prev_child, left_most):
            if child_node:
                if prev_child:
                    prev_child.next = child_node
                else:
                    left_most = child_node
                prev_child = child_node
            return prev_child, left_most

        if not root:
            return root

        leftmost = root

        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = process_child(curr.left, prev, leftmost)
                prev, leftmost = process_child(curr.right, prev, leftmost)
                curr = curr.next

        return root

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val in [p.val, q.val]:
            return root

        left_node = self.lowest_common_ancestor(root.left, p, q)
        right_node = self.lowest_common_ancestor(root.right, p, q)
        if left_node is not None and right_node is not None:
            return root
        return left_node or right_node
