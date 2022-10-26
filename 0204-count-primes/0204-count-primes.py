class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0 
        
        num_array = [False, False] + [True]*(n - 2)
        for i in range(2, int((n ** 0.5) + 1)):
            if num_array[i]:
                for j in range(i * i, n, i):
                    num_array[j] = False
                    
        return sum(num_array)
                
            
        