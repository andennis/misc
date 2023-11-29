from typing import Optional, List

from binary_tree import TreeNode


class BinaryTreeBuild:
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
