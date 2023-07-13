class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*n
        adj = [[] for _ in range(n)]
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        # print(adj, indegree)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        seen = 0    
        while queue:
            node = queue.popleft()
            seen += 1
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return seen == n
            
        