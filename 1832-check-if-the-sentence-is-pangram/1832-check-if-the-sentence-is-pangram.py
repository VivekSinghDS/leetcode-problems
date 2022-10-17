class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mapper = {}
        for i in range(26):
            mapper[i] = 0
            
        for char in sentence:
            mapper[ord(char) - ord('a')] += 1
        
        # print(mapper.values())
        return not 0 in mapper.values()
        