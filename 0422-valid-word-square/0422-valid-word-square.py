class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        vert_words = []
        try:
            for i in range(len(words)):
                string = ""
                for j in range(len(words[i])):

                    string += words[j][i]

                vert_words.append(string)
        except:
            return False
            
        return (vert_words) == words
                
            
            
        