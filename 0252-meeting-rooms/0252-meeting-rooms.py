class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        pre = None 
        
        for start, end in intervals:
            # print(start, end)
            if not pre:
                pre = [start, end]
                
            else:
                previous_start, previous_end = pre 
                # print(previous_start, previous_end, start, end)
                
                if previous_end > start:
                    return False
                
                pre = [start, end]
                
        return True
        