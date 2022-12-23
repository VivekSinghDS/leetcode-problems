# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = float('-inf')
        def dfs(node, level):
            nonlocal max_level
            if not node:
                max_level = max(max_level, level - 1)
                return 
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        queue = deque()
        queue.append((root, 0))
        res = 0
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node:
                    if not node.left and not node.right and level == max_level:
                        res += node.val
                        
                    else:
                        queue.append((node.left, level + 1))
                        queue.append((node.right, level + 1))
                        
                        
        return (res)
                
                
        