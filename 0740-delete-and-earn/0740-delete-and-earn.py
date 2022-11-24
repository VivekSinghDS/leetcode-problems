class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        @cache   
        def dfs(num):
            if num == 0:
                return 0
            
            if num == 1:
                return points[1]
            
            total = 0
            total = max(points[num] + dfs(num - 2), dfs(num - 1))
            return total
        
        return dfs(max_number)
        
        
                
                
                
            
            
            
            
            
            
        