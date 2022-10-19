class Solution:
    def numTrees(self, n: int) -> int:
        nums = [1]*(n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                
                total += (nums[left] * nums[right])
                
            nums[nodes] = total
            
        return nums[n]
                
        
        
        