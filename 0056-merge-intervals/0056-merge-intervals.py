class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        
        pre = None 
        
        for i in range(len(intervals)):
            if not pre:
                res.append(intervals[i])
                pre = intervals[i]
                
            else:
                pre_min, pre_max = pre
                
                if pre_max < intervals[i][0]:
                    res.append(intervals[i])
                    pre = intervals[i]
                    
                elif pre_max >= intervals[i][0]:
                    res.pop()
                    pre_max = max(pre_max, intervals[i][1])
                    res.append([pre_min, pre_max])
                    pre = [pre_min, pre_max]
                    
        return res
                    
                
            
        