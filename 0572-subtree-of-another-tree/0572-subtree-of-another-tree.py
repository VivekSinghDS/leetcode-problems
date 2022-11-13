# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root1, root2):
            if not root1 and not root2:
                return True 
            
            elif None in [root1, root2] or root1.val != root2.val:
                return False 
            
            return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
        
        if not root and not subRoot:
            return True 
        
        elif None in [root, subRoot]:
            return False 
        
        if isSame(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        