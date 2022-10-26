class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for cur, pre in prerequisites:
            graph[cur].append(pre)
            
        # print(graph)
            
        def dfs(seen, course):
            # print(seen, course)
            if course in seen:
                return False 
            
            elif graph[course] == []:
                return True
            
            seen.add(course)
            for pred in graph[course]:
                if not dfs(seen, pred):
                    return False 
            
            seen.remove(course)
            graph[course] = []
            return True
        
    
        seen = set()
        for i in range(numCourses):
            if not dfs(seen, i):
                return False 
            
        return True
                