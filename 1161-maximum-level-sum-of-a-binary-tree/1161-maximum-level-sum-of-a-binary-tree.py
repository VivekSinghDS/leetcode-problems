# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = deque()
        queue.append((root, 1))
        max_sum = float('-inf')
        
        while queue:
            current_level_sum = 0
            flag = False
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node:
                    flag = True
                    current_level_sum += node.val
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                    
            if flag and max_sum < current_level_sum:
                max_sum = current_level_sum 
                depth = level
                
        return depth
            
            
        