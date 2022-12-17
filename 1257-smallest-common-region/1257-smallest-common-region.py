class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        graph = {}
        
        for region in regions:
            for area in region[1:]:
                graph[area] = region[0]
        
        # print(graph)
        
        r1_copy = region1
        r2_copy = region2
        
        while region1 != region2:
            
            if graph.get(region1, False):
                region1 = graph[region1]
                
            else:
                region1 = r2_copy 
                
            if graph.get(region2, False):
                region2 = graph[region2]
                
            else:
                region2 = r1_copy
                
        return region1
                