from typing import Optional
from binary_tree import TreeNode


class BinaryTreeUnivalue:
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

    @staticmethod
    def count_unival_subtrees_v3(root: Optional[TreeNode]) -> int:
        def count_subtrees(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return True, 0

            is_left, l_count = count_subtrees(node.left)
            is_right, r_count = count_subtrees(node.right)
            if is_left and is_right:
                if node.left and node.val != node.left.val:
                    return False, l_count + r_count
                if node.right and node.val != node.right.val:
                    return False, l_count + r_count

                return True, l_count + r_count + 1

            return False, l_count + r_count

        if not root:
            return 0

        result = count_subtrees(root)
        return result[1]
