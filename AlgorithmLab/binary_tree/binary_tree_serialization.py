from typing import Optional
from collections import deque

from binary_tree import TreeNode


class BinaryTreeSerialization:
    def serialize_v1(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        left = self.serialize_v1(root.left)
        right = self.serialize_v1(root.right)

        if left and right:
            return "{}({},{})".format(root.val, left, right)
        if left:
            return "{}({})".format(root.val, left)
        if right:
            return "{}(,{})".format(root.val, right)
        return str(root.val)

    def deserialize_v1(self, data: str) -> Optional[TreeNode]:
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
        left_node = self.deserialize_v1(left_data)
        right_node = self.deserialize_v1(right_data)
        return TreeNode(int(data[:i]), left=left_node, right=right_node)

    def serialize_v2(self, root: Optional[TreeNode]) -> str:

        def build_preorder_tree(node: Optional[TreeNode]):
            if not node:
                return
            preorder.append(str(node.val))
            build_preorder_tree(node.left)
            build_preorder_tree(node.right)

        def build_inorder_tree(node: Optional[TreeNode]):
            if not node:
                return
            build_inorder_tree(node.left)
            inorder.append(str(node.val))
            build_inorder_tree(node.right)

        if not root:
            return ""

        preorder = []
        inorder = []
        build_preorder_tree(root)
        build_inorder_tree(root)
        return ",".join(preorder) + ":::" + ",".join(inorder)

    def deserialize_v2(self, data: str) -> Optional[TreeNode]:
        """
        The solution works only for the case if the node values are unique.
        The uniqueness is required by the inorder map
        """
        def build_nodes(start: int, end: int) -> Optional[TreeNode]:
            if not preorder:
                return None
            if start > end:
                return None

            val = int(preorder.popleft())
            i = inorder_map[val]
            left_node = build_nodes(start, i-1)
            right_node = build_nodes(i+1, end)
            return TreeNode(val, left=left_node, right=right_node)

        if not data:
            return None

        trvs = data.split(":::")
        if len(trvs) != 2 or not all(trvs):
            return None
        preorder = deque(trvs[0].split(","))
        inorder = trvs[1].split(",")
        inorder_map = {int(x): i for i, x in enumerate(inorder)}
        return build_nodes(0, len(preorder))

    def serialize_v3(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ","
        left = self.serialize_v3(root.left)
        right = self.serialize_v3(root.right)
        return "{},".format(root.val) + left + right

    def deserialize_v3(self, data: str) -> Optional[TreeNode]:

        def build_tree() -> Optional[TreeNode]:
            if len(nodes) == 0:
                return None

            val = nodes.popleft()
            if not val:
                return None
            left_node = build_tree()
            right_node = build_tree()
            return TreeNode(int(val), left=left_node, right=right_node)

        if not data:
            return None

        nodes = deque(data.split(","))
        return build_tree()
