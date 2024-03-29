# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        res = None
        def get_x(node):
            if not node:
                return None 
            
            left = get_x(node.left)
            right = get_x(node.right)
            if node.val == x:
                return node 
            
            if left:
                return left 
            
            if right:
                return right 
            
            return None
            
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)                
            return 1 + left + right
        
        
        x_node = get_x(root)
        left_count = dfs(x_node.left)
        right_count = dfs(x_node.right)
        
        parent_count = n - left_count - right_count - 1
        return ((parent_count > left_count + right_count) 
                or (left_count > right_count + parent_count) 
                or (right_count > left_count + parent_count))
        

                
            
        