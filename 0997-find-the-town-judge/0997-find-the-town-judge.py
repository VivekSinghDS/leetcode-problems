class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for judgee, judges in trust:
            graph[judgee].add(judges)
            
        flag = False 
        judge = None
        # print(graph)
        for key in range(1, n + 1):
            if not graph[key]:
                judge = key
                flag = True 
        # print(judge)       
        if not flag:
            return -1 
        
        flag = True 
        for key in range(1, n + 1):
            if key == judge:
                continue
            if judge not in graph[key]:
                flag = False
                
        return -1 if not flag else judge
                
        
        
            
        