# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        queue = deque()
        self.root = root
        self.root.val = 0
        self.hash_set = set()
        queue.append(self.root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    self.hash_set.add(node.val)
                    if node.left:
                        node.left.val = 2 * node.val + 1
                        queue.append(node.left)
                        
                    if node.right:
                        node.right.val = 2 * node.val + 2
                        queue.append(node.right)
                        
            
            
    def find(self, target: int) -> bool:
        return True if target in self.hash_set else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)