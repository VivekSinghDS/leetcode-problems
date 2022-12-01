# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return None 
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        
        queue = deque()
        queue.append((target, 0))
        seen = set()
        res = []
        while queue:
            if queue[0][1] == k:
                return [node.val for node, distance in queue]
            
            for _ in range(len(queue)):
                node, distance = queue.popleft()
                if node not in seen:
                    seen.add(node)
                    
                    for neighbor in [node.left, node.right, node.parent]:
                        if neighbor and neighbor not in seen:
                            queue.append((neighbor, distance + 1))
                            
        return []
                        
                        
                        
        