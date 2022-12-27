# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        
        queue.append((root, None, None))
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                node, grandparent, parent = queue.popleft()
                
                if node:
                    # print(node.val, level, grandparent, parent, res)
                     
                    if grandparent and grandparent % 2 == 0:
                        res += node.val 
                            
                    queue.append((node.left, parent, node.val))
                    queue.append((node.right, parent, node.val))
                    
        return res
        