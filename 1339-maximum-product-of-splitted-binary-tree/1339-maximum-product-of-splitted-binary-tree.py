# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        mod = 10**9 + 7
        def get_total(node):
            nonlocal total
            if not node:
                return 0 
            
            total += node.val 
            get_total(node.left)
            get_total(node.right)
            
        get_total(root)
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0 
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            cur_val = node.val + left_sum + right_sum 
            res = max(res, (total - cur_val) * cur_val)
            
            return cur_val
        
        dfs(root)
        return res % mod
            