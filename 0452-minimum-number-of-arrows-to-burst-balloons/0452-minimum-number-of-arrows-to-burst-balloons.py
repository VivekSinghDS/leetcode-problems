class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        mapper = {}
        pre = None 
        for i, (x1, x2) in enumerate(points):
            if pre:
                pre_x1, pre_x2 = pre 
                
                if x1 - pre_x2 <= 0:
                    mapper[(max(x1, pre_x1), min(x2, pre_x2))] = mapper[(pre_x1, pre_x2)]
                    if (max(x1, pre_x1), min(x2, pre_x2)) != (pre_x1, pre_x2):
                        mapper.pop((pre_x1, pre_x2))
                    
                    pre = (max(x1, pre_x1), min(x2, pre_x2))
                    
                else:
                    mapper[(x1, x2)] = i
                    pre = (x1, x2)
                    
            else:
                mapper[(x1, x2)] = i
                pre = (x1, x2)

        
        # print(mapper)
        return len((mapper.values()))
        