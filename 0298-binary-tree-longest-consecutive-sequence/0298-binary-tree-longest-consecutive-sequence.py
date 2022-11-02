# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 1))
        max_len = 1
        
        while queue:
            for _ in range(len(queue)):
                node, score = queue.popleft()
                if node:
                    if node.left:
                        if node.left.val - 1 == node.val:
                            queue.append((node.left, score + 1))
                            max_len = max(max_len, score + 1)
                            
                        else:
                            queue.append((node.left, 1))
                            
                    if node.right:
                        if node.right.val - 1 == node.val:
                            queue.append((node.right, score + 1))
                            max_len = max(max_len, score + 1)
                            
                        else:
                            queue.append((node.right, 1))
                            
        return max_len
        
        