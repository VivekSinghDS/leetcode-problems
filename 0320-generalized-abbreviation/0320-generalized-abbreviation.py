class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def backtrack(pos, cur_string, count):
            if pos == len(word):
                res.append(cur_string + str(count if count > 0 else ""))
                return 

            else:
                backtrack(pos + 1, cur_string, count + 1)
                backtrack(pos + 1, cur_string + str(count if count > 0 else "") + word[pos], 0)
        
        backtrack(0, "", 0)
        return res
        