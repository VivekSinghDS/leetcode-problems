# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return 0 
            
            current = (node == p or node == q)
            left = dfs(node.left)
            right = dfs(node.right)
            
            if ((left and right) or (left and current)
               or (right and current)):
                return node
            
            return current or left or right
            
            
        res_node = dfs(root)
        if res_node is None or res_node is True:
            return None 
        
        else:
            return res_node 
        