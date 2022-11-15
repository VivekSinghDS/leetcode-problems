# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def parenting_dfs(node, parent):
            if node:
                node.parent = parent 
                parenting_dfs(node.left, node)
                parenting_dfs(node.right, node)
                
        parenting_dfs(root, None)
        
        queue = deque()
        queue.append((target, 0))
        seen = set()
        seen.add(target)
        while queue:
            if queue[0][1] == k:
                return [node.val for node, _ in queue]
            
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node:
                    if node.left and node.left not in seen:
                        seen.add(node.left)
                        queue.append((node.left, level + 1))
                        
                    if node.right and node.right not in seen:
                        seen.add(node.right)
                        queue.append((node.right, level + 1))
                        
                    if node.parent and node.parent not in seen:
                        seen.add(node.parent)
                        queue.append((node.parent, level + 1))
                        
        return []
                
            