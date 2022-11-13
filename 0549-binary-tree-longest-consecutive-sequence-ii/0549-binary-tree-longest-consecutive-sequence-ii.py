# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_count = 0
        
        def dfs(node):
            nonlocal max_count
            if not node:
                return [0, 0] # inc, dec
            
            
            inc = dec = 1
            if node.left:
                left = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = left[1] + 1
                    
                elif node.val == node.left.val - 1:
                    inc = left[0] + 1
                    
            if node.right:
                right = dfs(node.right)
                if node.val == node.right.val - 1:
                    inc = max(inc, right[0] + 1)
                    
                elif node.val == node.right.val + 1:
                    dec = max(dec, right[1] + 1)
            
            max_count = max(max_count, inc + dec - 1)
            return [inc, dec]
        
        dfs(root)
        return max_count
                
                
            
            
            
            
            
        