class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # letters.sort()
        value = bisect_right(letters, target)
        return letters[value] if value < len(letters) else letters[0]
            
            
        