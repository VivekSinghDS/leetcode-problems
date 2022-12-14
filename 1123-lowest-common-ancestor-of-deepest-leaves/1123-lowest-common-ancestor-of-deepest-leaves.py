# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        count = 0
        def get_max_depth(node, level):
            nonlocal count
            if not node:
                count = max(count, level - 1)
                return
                
            get_max_depth(node.left, level + 1)
            get_max_depth(node.right, level + 1)
        
        get_max_depth(root, 0)
        def getLCA(node, depth):
            if not node:
                return None
            
            if depth == count:
                return node 
            
            left = getLCA(node.left, depth + 1)
            right = getLCA(node.right, depth + 1)
            
            if left and right:
                return node
            
            elif left and not right:
                return left 
            
            elif right and not left:
                return right
            
            return None 
        
        return getLCA(root, 0)
            
        
            
            