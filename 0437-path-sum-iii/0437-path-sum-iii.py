# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def dfs(node, current_sum):
            nonlocal count 
            
            if not node:
                return 
            
            current_sum += node.val 
            
            if current_sum == targetSum:
                count += 1
                
            count += h[current_sum - targetSum]
            h[current_sum] += 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            h[current_sum] -= 1
            
        h = defaultdict(int)
        dfs(root, 0)
        return count
        