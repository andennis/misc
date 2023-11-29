from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class BinaryTreeTraversal:
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
        i = next((i for i, x in enumerate(result[::-1]) if x is not None))
        return result[:len(result) - i]
