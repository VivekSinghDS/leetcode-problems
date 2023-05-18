class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree_nodes = []
        i_set = set()
        
        for source, target in edges:
            graph[source].append(target)
        
        for i in range(n):
            for nodes in graph[i]:
                i_set.add(nodes)
    
        def dfs(node):
            if node in seen:
                return 
            
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        seen = set()
        res = []
        # print(i_set)
        for i in range(n):
            if i not in i_set and i not in seen:
                res.append(i)
                dfs(i)
                # print(seen)
                
        return res