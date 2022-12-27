# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        
        queue.append((root, None))
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                
                if node:
                    if node.left:
                        if parent and parent % 2 == 0:
                            res += node.left.val
                            
                    if node.right:
                        if parent and parent % 2 == 0:
                            res += node.right.val
                            
                    queue.append((node.left, node.val))
                    queue.append((node.right, node.val))
                    
        return res
        