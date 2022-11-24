# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, prev):
            if not node:
                return None 
            
            node.parent = prev
            dfs(node.left, node)
            dfs(node.right, node)
            
        def find(target):
            queue = deque()
            queue.append(root)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        if node.val == k:
                            return node 
                        queue.append(node.left)
                        queue.append(node.right)
                        
                
        dfs(root, None)
        queue = deque()
        target = find(k)
        queue.append(target)
        seen = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if not node.left and not node.right:
                        return node.val
                    for neighbor in [node.left, node.right, node.parent]:
                        if neighbor and neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
                            if not neighbor.left and not neighbor.right:
                                return neighbor.val
                            
        # return root.val
                    
        