class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = defaultdict(list)
        
        for word in strs:
            mapper = [0]*26
            
            for char in word:
                mapper[ord(char) - ord('a')] += 1
                
            seen[tuple(mapper)].append(word)
            
        return seen.values()
        
            