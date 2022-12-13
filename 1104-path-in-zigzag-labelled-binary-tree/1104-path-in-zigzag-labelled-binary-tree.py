class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        node_count = 1
        level = 1
        while node_count * 2 <= label:
            node_count *= 2
            level += 1
            
        while label:
            res.append(label)
            level_max = (2 ** level) - 1
            level_min = 2 ** (level - 1)
            
            label = int((level_max + level_min - label) / 2)
            level -= 1
            
        return res[::-1]