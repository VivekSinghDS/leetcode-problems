class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        
        graph = defaultdict(list)
        degree = [0]*n
        for to, from_ in roads:
            graph[to].append(from_)
            graph[from_].append(to)
            
            degree[to] += 1
            degree[from_] += 1
            
        # print(graph)
        # print(degree)
        
        queue = deque()
        for i in range(n):
            if degree[i] == 1 and i != 0:
                queue.append(i)
                
        representatives = [1]*n
        
        fuel = 0 
        
        while queue:
            node = queue.popleft()
            print(node)
            fuel += ceil(representatives[node] / seats)
            
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                
                if degree[neighbor] == 1 and neighbor != 0:
                    queue.append(neighbor)
                    
        return fuel
        
        