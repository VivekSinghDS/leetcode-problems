class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = defaultdict(list)
        
        for letter in strs:
            
            mapper = [0]*(26)
            for char in letter:
                mapper[ord(char) - ord("a")] += 1
                
            seen[tuple(mapper)].append(letter)
            
        return seen.values()
            