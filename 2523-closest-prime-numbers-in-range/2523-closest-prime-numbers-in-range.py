class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def get_prime_numbers_in_range(left, right):
            nums_array = [False, False] + [True]*(right - 2)
            
            for i in range(2, int((right ** 0.5) + 1)):
                if nums_array[i]:   
                    for j in range(i*i, right, i):
                        nums_array[j] = False
                        
            return nums_array
        
        number_list = get_prime_numbers_in_range(1, right + 1)
        pre = None
        ans = float('inf')
        res = [-1,-1]
        for number, boolean in enumerate(number_list):
            if number < left:
                continue
            if number_list[number]:
                if pre:
                    if ans > number - pre:
                        res = [pre, number]
                        ans = number - pre
                        
                pre = number
        return res
                    