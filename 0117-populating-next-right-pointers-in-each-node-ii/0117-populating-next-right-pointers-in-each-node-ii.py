"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)
        
        while queue:
            prev = None 
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if prev:
                        prev.next = node 
                        
                    queue.append(node.left)
                    queue.append(node.right)
                    
                    prev = node 
                    
        return root
        