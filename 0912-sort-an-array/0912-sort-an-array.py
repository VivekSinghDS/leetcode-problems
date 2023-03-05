class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mapper = defaultdict(int)
        
        for n in nums:
            mapper[n] += 1
        
        min_val = min(mapper.keys())
        max_val = max(mapper.keys())
        output = []
        for key in range(min_val, max_val + 1):
            if key in mapper:
                output.extend([key]*mapper[key])
                
        return output