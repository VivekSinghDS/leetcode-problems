# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val, root, None)
            return new
        
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node:
                    if level + 1 == depth:
                        left = node.left
                        right = node.right
                        
                        new_node_1 = TreeNode(val)
                        new_node_2 = TreeNode(val)
                        node.left = new_node_1
                        node.right = new_node_2
                        
                        new_node_1.left = left
                        new_node_2.right = right
  
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
        return root
        
        
                        
        