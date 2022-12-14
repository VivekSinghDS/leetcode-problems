# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 0 
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            if left_sum + right_sum == node.val:
                count += 1
                
            return (left_sum + right_sum + node.val)

        dfs(root)
        return count