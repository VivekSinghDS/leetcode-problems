class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            seen.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)
            
        graph = defaultdict(list)
        m, n = len(isConnected), len(isConnected[0])
        for r in range(m):
            for c in range(n):
                if isConnected[r][c] == 1 and r != c:
                    graph[r + 1].append(c + 1)
                    
        ans = 0 
        seen = set()
        for i in range(1, len(isConnected) + 1):
            if i not in seen:
                dfs(i)
                ans += 1
                
        return ans
                    
        
        