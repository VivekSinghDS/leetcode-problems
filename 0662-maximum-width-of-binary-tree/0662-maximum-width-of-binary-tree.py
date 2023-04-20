# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        res = 0
        
        while queue:
            start = queue[0][1]
            end = queue[-1][1]
            res = max(res, end - start + 1)
            
            for _ in range(len(queue)):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*i + 1))
                    
                if node.right:
                    queue.append((node.right, 2*i + 2))
                    
        return res
        