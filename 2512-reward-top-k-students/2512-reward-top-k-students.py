class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        points = []

        for i, rep in enumerate(report):
            score = 0
            rep = rep.split(' ')
            for word in rep:
                if word in positive:
                    score += 3
                    
                if word in negative:
                    score -= 1
            points.append((-score, student_id[i]))        
                    
        res = []
        heapify(points)
        while k > 0:
            value = heapq.heappop(points)
            res.append(value[1])
            k -= 1
        return res
        
        

            
            
                    
        