class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = str(int("".join(str(x) for x in num)) + k)
        num = [int(n) for n in num]
        return num
        