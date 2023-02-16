# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        @cache
        def dfs(node, level):
            nonlocal res
            if node:
                res = max(res, level)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        
        dfs(root, 1)
        return res
        