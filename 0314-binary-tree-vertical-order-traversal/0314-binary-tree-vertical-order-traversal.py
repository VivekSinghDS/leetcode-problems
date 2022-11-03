# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        queue.append((root, 0))
        mapper = defaultdict(list)
        
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node:
                    mapper[level].append(node.val)
                    queue.append((node.left, level - 1))
                    queue.append((node.right, level + 1))
                    
        min_level, max_level = min(mapper.keys()), max(mapper.keys())
        res = []
        for i in range(min_level, max_level + 1):
            res.append(mapper[i])
            
        return res
            
                    
        