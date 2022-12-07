# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque()
        queue.append(root)
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if low <= node.val <= high:
                        res += node.val
                        
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return res
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cur_max = root.val
#         cur_min = root.val
#         def find_max(node):
#             nonlocal cur_max
#             if not node:
#                 return float('-inf') 
            
#             if node.right:
#                 right = find_max(node.right)
#                 cur_max = max(cur_max, right)
                
#             elif node.left:
#                 left = find_max(node.left)
#                 cur_max = max(cur_max, left)
                
#             return node.val
        
#         def find_min(node):
#             nonlocal cur_min
#             if not node:
#                 return float('inf')
            
#             if node.left:
#                 left = find_min(node.left)
#                 cur_min = min(cur_min, left)
                
#             elif node.right:
#                 right = find_min(node.right)
#                 cur_min = min(cur_min, right)
                
#             return node.val
            
            
        
#         find_max(root)
#         find_min(root)
#         print(cur_max - cur_min)
            
        