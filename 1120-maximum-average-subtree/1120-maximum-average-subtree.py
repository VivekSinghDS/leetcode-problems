# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            # print(node)
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            current_sum = node.val + left_sum + right_sum
            res = max(res, current_sum / (left_count + right_count + 1))
            
            return (current_sum, left_count + right_count + 1)
        
        dfs(root)
        return res
            
            
            
            
            
            
        