class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        res = 1
        
        for i in range(len(points)):
            x1, y1 = points[i]
            counter = defaultdict(int)
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                
                slope = (y2 - y1) / (x2 - x1) if x2 -x1 != 0 else float('inf')
                counter[slope] += 1
                
                res = max(res, counter[slope] + 1)
                
        return res
                

        
        