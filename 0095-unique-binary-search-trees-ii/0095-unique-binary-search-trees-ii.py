# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize = None)
        def generate(start, end):
            all_trees = []
            if start > end:
                return [None,]
            
            elif start == end:
                node = TreeNode(start, None, None)
                
                all_trees.append(node)
                return all_trees
            
            else:
                for i in range(start, end + 1):
                    left = generate(start, i - 1)
                    right = generate(i + 1, end)
                    
                    for val1 in left:
                        for val2 in right:
                            node = TreeNode(i)
                            node.left = val1
                            node.right = val2
                            
                            all_trees.append(node)
                            
                return all_trees
            
        return generate(1, n) if n else []
            
            
                
        