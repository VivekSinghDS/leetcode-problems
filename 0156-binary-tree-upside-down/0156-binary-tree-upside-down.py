# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = None 
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        def dfs(node):
            nonlocal new_root
            if not node:
                return None
            
            if not node.left and not node.right:
                return node 
            
            left_ = dfs(node.left)
            right_ = dfs(node.right)
            
            if new_root is None:
                new_root = left_
                
            if left_:
                left_.right = node
                 
            node.left = None 
            
            if right_:
                
                left_.left = right_
            
            node.right = None
                
            
            return node
        
        dfs(root)
        return new_root
                
                
            
        