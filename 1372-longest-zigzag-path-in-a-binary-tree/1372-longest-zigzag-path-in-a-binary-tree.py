# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node, goLeft, steps):
            nonlocal res
            if node:
                res = max(res, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                    
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
                    
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res
            
            
            
            
            
            
        