class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
            
            
        def dfs(node):
            nonlocal count
            if node not in seen:
                seen.add(node)
                count += 1
                for neighbor in graph[node]:
                    dfs(neighbor)
                    
        
        
        seen = set()
        res = []
        for i in range(n):
            if i not in seen:
                count = 0
                dfs(i)
                res.append(count)
        if len(res) == 1:
            return 0
        
        total = sum(res)
        ans = 0
        running_sum = 0
        for n in res:
            running_sum += n
            ans += n*(total - running_sum)
            
        return(ans)
        