class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        first = letters[0]
        
        for letter in letters:
            if ord(target) < ord(letter):
                return letter
        return first
            
            
        