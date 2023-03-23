class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = defaultdict(list)
        for source, target in connections:
            graph[source].append(target)
            graph[target].append(source)
            
        res = []
        
        @cache
        def dfs(node):
            nonlocal count
            if node not in seen:
                # print(node, seen)
                count += 1
                seen.add(node)
                
                for neighbor in graph[node]:
                    dfs(neighbor)

        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                count = 0
                dfs(i)
                if i > 0:
                    ans += 1
                
                
        return ans

                
        