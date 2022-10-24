# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None 
            
            left_part = dfs(node.left)
            right_part = dfs(node.right)
            
            if node.left:
                left_part.right = node.right
                node.right = node.left 
                node.left = None 
                
            return right_part or left_part or node
        
        dfs(root)
                
        