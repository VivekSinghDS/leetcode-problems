class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache 
        def solve(i):
            if i == 1:
                return k 
            
            if i == 2:
                return k ** 2
            
            return (solve(i - 1) + solve(i - 2))*(k - 1)
        
        return solve(n)
    
    '''
    no_of_ways(i) = no_of_ways_similar(i) + no_of_ways_diff(i)
    
    for -> no_of_ways_diff(i - 1) = no_of_ways(i - 1) * (k - 1) ... The reason being we can color (k - 1) colors to the last fence
    for -> no_of_ways_similar(i) = no_of_ways_diff(i - 1) = no_of_ways(i - 2)*(k - 1)
    
    adding both of them 
    no_of_ways(i) = no_of_ways(i - 1) * (k - 1) + no_of_ways(i - 2)*(k - 2)
    
    
    '''
            
            
        