from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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
    def tree_to_level_list(root: TreeNode) -> List[int]:
        if not root:
            return []
        nodes = [root]
        result = []
        while any(nodes):
            level_len = len(nodes)
            for _ in range(level_len):
                node = nodes.pop(0)
                result.append(node.val if node else None)
                if node:
                    nodes.extend([node.left, node.right])
        return result

    def build_tree_inorder_postorder_iteratively(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        i_in = 0
        in_vals = inorder.copy()
        post_vals = postorder.copy()
        self.nodes = []
        while i_in < len(in_vals) > 1:
            ln = len(in_vals)
            if in_vals[i_in] == post_vals[0]:
                if i_in + 1 < ln \
                        and in_vals[i_in+1] == post_vals[1]:
                    self._get_node(in_vals[i_in+1], left_val=in_vals[i_in])
                    del in_vals[i_in:i_in+1]
                    del post_vals[0:1]
                elif i_in + 2 < ln \
                        and in_vals[i_in+1] == post_vals[2] \
                        and in_vals[i_in+2] == post_vals[1]:
                    node = self._get_node(in_vals[i_in+1], left_val=in_vals[i_in], right_val=in_vals[i_in+2])
                    del in_vals[i_in:i_in+2]
                    del post_vals[0:2]
                    in_vals[i_in] = node.val
                elif i_in + 1 < ln:
                    self._get_node(in_vals[i_in+1], left_val=in_vals[i_in])
                    del in_vals[i_in:i_in+1]
                    del post_vals[0:1]
                else:
                    raise Exception('inconsistent data')
                i_in = 0
            elif in_vals[i_in] == post_vals[1] \
                    and in_vals[i_in+1] == post_vals[0] and i_in + 1 < ln:
                self._get_node(in_vals[i_in], right_val=in_vals[i_in + 1])
                del in_vals[i_in+1:i_in+2]
                del post_vals[0:1]
                i_in = 0
            else:
                i_in += 1

        return self._get_node(in_vals[0])

    def _get_node(
            self,
            root_val: int,
            left_val: Optional[int] = None,
            right_val: Optional[int] = None
    ) -> Optional[TreeNode]:
        if root_val is None:
            raise TypeError("The value root_val must not be None")

        left_node = None
        if left_val is not None:
            left_node = next((x for x in self.nodes if x.val == left_val), None)
            if not left_node:
                left_node = TreeNode(left_val)
                self.nodes.append(left_node)

        right_node = None
        if right_val is not None:
            right_node = next((x for x in self.nodes if x.val == right_val), None)
            if not right_node:
                right_node = TreeNode(right_val)
                self.nodes.append(right_node)

        root_node = next((x for x in self.nodes if x.val == root_val), None)
        if not root_node:
            root_node = TreeNode(root_val, left=left_node, right=right_node)
            self.nodes.append(root_node)
        else:
            root_node.left = left_node or root_node.left
            root_node.right = right_node or root_node.right

        return root_node

    def build_tree_inorder_postorder_recursively_v1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        return self._build_tree_inorder_postorder_recursively(None, 0, 0, len(inorder) - 1)

    def _build_tree_inorder_postorder_recursively(self,
                                                  node: Optional[TreeNode],
                                                  in_i: int,
                                                  post_i: int,
                                                  post_last_i: int) -> Optional[TreeNode]:
        if post_i > post_last_i:
            return node

        if self.inorder[in_i] == self.postorder[post_i]:
            return self._build_tree_inorder_postorder_recursively(TreeNode(self.inorder[in_i], left=node), in_i + 1, post_i + 1, post_last_i)

        if in_i+1 < len(self.inorder) \
                and self.inorder[in_i] == self.postorder[post_i+1] \
                and self.inorder[in_i+1] == self.postorder[post_i]:
            new_node = TreeNode(self.inorder[in_i], left=node, right=TreeNode(self.inorder[in_i+1]))
            return self._build_tree_inorder_postorder_recursively(new_node, in_i + 2, post_i + 2, post_last_i)

        i = self.postorder.index(self.inorder[in_i])
        right_node = self._build_tree_inorder_postorder_recursively(None, in_i + 1, post_i, i - 1)
        new_node = TreeNode(self.inorder[in_i], left=node, right=right_node)
        return self._build_tree_inorder_postorder_recursively(new_node, in_i + i - post_i + 1, i + 1, post_last_i)

    @staticmethod
    def build_tree_inorder_postorder_recursively_v2(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build_nodes(left, right):
            if left > right:
                return None
            node = TreeNode(postorder.pop())
            i = maps[node.val]
            node.right = build_nodes(i + 1, right)
            node.left = build_nodes(left, i - 1)
            return node

        maps = {v: i for i, v in enumerate(inorder)}
        return build_nodes(0, len(inorder) - 1)

    @staticmethod
    def build_tree_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_nodes(left, right):
            if left > right:
                return None
            node = TreeNode(preorder.pop(0))
            i = inorder_map[node.val]
            node.left = build_nodes(left, i - 1)
            node.right = build_nodes(i + 1, right)
            return node

        inorder_map = {v: i for i, v in enumerate(inorder)}
        return build_nodes(0, len(inorder) - 1)

    @staticmethod
    def connect_right_nodes_v1(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes = [root]
        while nodes:
            nodes = [x for x in nodes if x is not None]
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i + 1]

            level_num = len(nodes)
            nodes2 = nodes
            nodes = [None] * level_num * 2
            for i in range(level_num):
                node = nodes2[i]
                nodes[i*2] = node.left
                nodes[i*2 + 1] = node.right

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

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        if left and right:
            return "{}({},{})".format(root.val, left, right)
        if left:
            return "{}({})".format(root.val, left)
        if right:
            return "{}(,{})".format(root.val, right)
        return str(root.val)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def parse_child_nodes(data: str) -> (str, str):
            pr_i = data.find("(")
            cm_i = data.find(",")
            if pr_i != -1 and pr_i < cm_i:
                n_left = n_right = 0
                for j in range(pr_i, len(data)):
                    if data[j] == "(":
                        n_left += 1
                    elif data[j] == ")":
                        n_right += 1
                    if n_left == n_right:
                        cm_i = j+1
                        break

            if cm_i != -1:
                return data[:cm_i], data[cm_i+1:]

            return data, ""

        if not data:
            return None

        i = data.find("(")
        if i == -1:
            return TreeNode(int(data))

        left_data, right_data = parse_child_nodes(data[i+1:-1])
        left_node = self.deserialize(left_data)
        right_node = self.deserialize(right_data)
        return TreeNode(int(data[:i]), left=left_node, right=right_node)

