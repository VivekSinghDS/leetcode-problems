class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def sliding_window(char):
            res = 0
            l = 0
            false_count = 0 
            for r in range(len(answerKey)):
                if answerKey[r] == char:
                    false_count += 1

                while false_count > k:
                    if answerKey[l] == char:
                        false_count -= 1

                    l += 1

                res = max(res, r - l + 1)
                
            return res
        return max(sliding_window("T"), sliding_window("F"))
                
        