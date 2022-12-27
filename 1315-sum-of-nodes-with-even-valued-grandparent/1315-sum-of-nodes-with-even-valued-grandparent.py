# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        
        queue.append((root, 0, None, None))
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                node, level, grandparent, parent = queue.popleft()
                
                if node:
                    # print(node.val, level, grandparent, parent, res)
                    if level != 0:
                        if grandparent and grandparent % 2 == 0:
                            res += node.val 
                            
                    queue.append((node.left, level + 1, parent, node.val))
                    queue.append((node.right, level + 1, parent, node.val))
                    
        return res
        