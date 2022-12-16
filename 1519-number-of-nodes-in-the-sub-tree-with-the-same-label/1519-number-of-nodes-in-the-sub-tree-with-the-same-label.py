class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [0] * n
        seen = set()
        seen.add(0)
        tree = defaultdict(list)
        for parent, child in edges:
            tree[parent].append(child)
            tree[child].append(parent)
            
        def dfs(node):
            counter = Counter(labels[node])
            for neighbor in tree[node]:
                if neighbor in seen:
                    continue   
                seen.add(neighbor)
                counter += dfs(neighbor)
                
            res[node] = counter.get(labels[node])

            return counter
        
        
        dfs(0)
        return res
        
        
                
                
        