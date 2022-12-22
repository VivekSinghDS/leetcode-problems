class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
            
        ans = [0]*n
        count = [1]*n
        # print('graph is ', graph)
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
                    
        dfs(0, -1)
        # print('count is ', count)
        # print('ans in ', ans)
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)
                    
        dfs2(0, -1)
        return ans
                    

        '''
        def bfs(start):
            queue = deque()
            queue.append((start, 0))
            seen = set()
            seen.add(start)
            res = 0
            
            while queue:
                node, distance = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, distance + 1))
                        
                        res += distance + 1
                        
            return res
                        
        return [bfs(i) for i in range(n)]
        '''   
        