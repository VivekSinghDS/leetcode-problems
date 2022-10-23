# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, ""))
        res = 0
        while queue:
            for _ in range(len(queue)):
                node, value = queue.popleft()
                if node:
                    if not node.left and not node.right:
                        # print(value, node.val)
                        ans = value + str(node.val)
                        res += int(ans)
                        
                    queue.append((node.left, value + str(node.val)))
                    queue.append((node.right, value + str(node.val)))
                    
        return res
                    
        