class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        previous = [None, -1] 
        res = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                previous_value, previous_index = previous
                if not previous_value:
                    previous = [word1, i]
                    
                elif previous_value == word1:
                    if word1 == word2:
                        res = min(res, i - previous_index)
                    previous = [word1, i]
                    
                elif previous_value == word2:
                    # print('here')
                    res = min(res, i - previous_index)
                    previous = [word1, i]
                    
            elif wordsDict[i] == word2:
                previous_value, previous_index = previous
                if not previous_value:
                    previous = [word2, i]
                    
                elif previous_value == word2:
                    if word1 == word2:
                        res = min(res, i - previous_index)
                    previous = [word2, i]
                    
                elif previous_value == word1 or word1 == word2:
                    # print('here 2')
                    res = min(res, i - previous_index)
                    previous = [word2, i]
                    
        return res
                
                    
        