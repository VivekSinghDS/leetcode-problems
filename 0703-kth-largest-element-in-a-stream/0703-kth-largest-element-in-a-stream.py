class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k
        

    def add(self, val: int) -> int:
        
        index = bisect_left(self.nums, val)
        if index == len(self.nums):
            self.nums.append(val)
        else:
            self.nums.insert(index, val)
        # print(self.nums)
        return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)