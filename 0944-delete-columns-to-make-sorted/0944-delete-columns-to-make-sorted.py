class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        
        for c in range(cols):
            cur_str = ""
            
            for r in range(rows):
                
                # print(c, strs[c][r])
                cur_str += strs[r][c]
                
            # print('-'*10)
            # print("".join(sorted(cur_str)), cur_str)
            if "".join(sorted(cur_str)) != cur_str:
                count += 1
                
        return count
                
        