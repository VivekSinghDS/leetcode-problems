# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        max_depth = 0
        def get_maximum_depth(node, level):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth, level - 1)
                return
        
            get_maximum_depth(node.left, level + 1)
            get_maximum_depth(node.right, level + 1)
                
        get_maximum_depth(root, 0)
        
        def dfs(node, level):
            if not node:
                return None
            
            if level == max_depth:
                return node 
            
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            if left and right:
                return node 
            return left if left else right
        
            
        return dfs(root, 0)
                
        
                
            
            
        