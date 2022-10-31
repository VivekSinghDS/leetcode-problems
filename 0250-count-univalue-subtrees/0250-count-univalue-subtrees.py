# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return None
            
            left_part = dfs(node.left)
            right_part = dfs(node.right)
            
            if left_part is None and right_part is None:
                res += 1
                return node.val
            
            if not left_part and node.val == right_part:
                res += 1
                return node.val
            
            if not right_part and left_part == node.val:
                res += 1
                return node.val
            
            if left_part and right_part and left_part == right_part == node.val:
                res += 1
                return node.val
            
            else:
                return "Nothing here"
            
        dfs(root)
        return res
                
                
            
            
            
            
            
            
            
        