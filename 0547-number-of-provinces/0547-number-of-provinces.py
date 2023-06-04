
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        total = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i == j:
                    total += 1
                    continue 
                if isConnected[i][j]:
                    graph[i + 1].append(j + 1)
        # print(graph, total)
        def dfs(node):
            if node not in seen:
                seen.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
        
        count = 0
        seen = set()
        for i in range(1, total + 1):
            if i not in seen:
                dfs(i)
                count += 1
                
        return count
            
            
        