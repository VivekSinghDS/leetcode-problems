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
        blank_somewhere = False 
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left and blank_somewhere:
                    return False 
                
                elif node.left:
                    queue.append(node.left)
                    
                else:
                    blank_somewhere = True
                    
                if node.right and blank_somewhere:
                    return False 
                
                elif node.right:
                    queue.append(node.right)
                    
                else:
                    blank_somewhere = True
                    
        return True
                    
        