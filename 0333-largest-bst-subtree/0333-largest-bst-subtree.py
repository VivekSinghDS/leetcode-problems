# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def dfs(node):
            nonlocal res
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            l_res, l_count, l_min, l_max = dfs(node.left)
            r_res, r_count, r_min, r_max = dfs(node.right)
            
            if l_res and r_res and l_max < node.val < r_min:
                res = max(res, l_count + r_count + 1)
                return (True, l_count + r_count + 1, min(l_min, node.val), max(node.val, r_max))
            
            return (False, 0, float('inf'), float('-inf'))
        
        dfs(root)
        return res
                