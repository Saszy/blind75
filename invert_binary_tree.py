# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

            # Swap the left and right
        root.left, root.right = root.right, root.left

        # recursively swap the left and right nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
