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
        
        if x == root.val:
            left_size = dfs(root.left)
            right_size = dfs(root.right)
            
            if left_size == right_size:
                return False
            else:
                return True
        else:
            x_node = get_x(root)
            
            left_count = dfs(x_node.left)
            right_count = dfs(x_node.right)
            # print(left_count, right_count)
            parent_count = n - left_count - right_count - 1
            if (parent_count > left_count + right_count or 
                left_count > parent_count + right_count or 
                right_count > parent_count + left_count):
                return True 
            
            else:
                return False
            
            
            
        # print(res, n - res)
                
            
        