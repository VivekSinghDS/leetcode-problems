# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        dif = float('inf')
        pre = None 
        def dfs(node):
            nonlocal dif, pre
            
            if not node:
                return None 
            
            dfs(node.left)
            if pre:
                dif = min(abs(node.val - pre.val), dif)
            pre = node
            dfs(node.right)
            
        dfs(root)
        return dif
        