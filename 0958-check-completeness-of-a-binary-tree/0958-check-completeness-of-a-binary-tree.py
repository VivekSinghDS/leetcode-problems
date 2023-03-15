# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        previous_node = root 
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if not previous_node:
                        return False
                    
                    queue.append(node.left)
                    queue.append(node.right)
                previous_node = node 
                
        return True
                    
            
                    
                
        