class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        nums = [[] for i in range(len(nums) + 1)]
        
        for key in counter:
            nums[counter[key]].append(key)
        
        # print(nums)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]:
                for element in nums[i]:
                    res.append(element)
                    k -= 1
                    if k == 0:
                        return res
