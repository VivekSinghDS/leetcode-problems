class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        
        def dfs(manager):
            time = informTime[manager]
            child_count = 0
            for neighbor in graph[manager]:
                child_count = max(child_count, dfs(neighbor))
                
                
            return time + child_count
        
        return dfs(headID)
            
        