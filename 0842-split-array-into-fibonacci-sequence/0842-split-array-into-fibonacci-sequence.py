class Solution:
    def splitIntoFibonacci(self, nums: str) -> List[int]:
        for i in range(min(10, len(nums))):
            x = nums[:i + 1]
            if x != "0" and x.startswith('0'):
                break
                
            a = int(x)
            
            for j in range(i + 1, min(i + 10, len(nums))):
                y = nums[i + 1: j + 1]
                if y != '0' and y.startswith('0'):
                    break
                    
                b = int(y)
                fib = [a, b]
                k = j + 1
                
                while k < len(nums):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    
                    if nxt <= 2 ** 31 - 1 and nums[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                        
                    else:
                        break
                        
                else:
                    if len(fib) >= 3:
                        return fib
                    
        return []
        
    
            
        