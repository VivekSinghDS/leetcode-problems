class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def get_prime_factors(n):
            res = set()
            nums_array = [False, False] + [True]*(n - 2)
            # print(2, int((n * 0.5) + 1))

            for i in range(2, int((n * 0.5) + 1)):
                # print('i is ', i)
                if nums_array[i]:
                    if n % i == 0:
                        res.add(i)
                    for j in range(i, n, i):
                        # print(j)
                        nums_array[j] = False
                        
            if not res:
                res.add(n)
                        
            return res
        
        # print(get_prime_factors(2))
        ans = set()
        for n in nums:
            prime_factors = get_prime_factors(n)
            
            for factor in prime_factors:
                ans.add(factor)
                
        return len(ans)