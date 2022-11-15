# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def left_size(node):
            if not node:
                return 0
            
            return 1 + left_size(node.left)
        
        def right_size(node):
            if not node:
                return 0 
            
            return 1 + right_size(node.right)
    
            
        left = left_size(root)
        right = right_size(root)
            
        if left > right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        else:
            return (2 ** left) - 1
        