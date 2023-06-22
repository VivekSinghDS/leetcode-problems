class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def insert_elements(root, set_name):
            queue = deque()
            queue.append(root)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        set_name.add(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                        
            return set_name
        set_1 = set()
        set_2 = set()
        set_1 = insert_elements(root1, set_1)
        set_2 = insert_elements(root2, set_2)
        for element in set_1:
            if (target - element) in set_2:
                return True 
            
        return False
        