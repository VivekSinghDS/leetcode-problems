class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key = lambda x:x[0])
        slope = None
        for i in range(1, len(coordinates)):
            y2, x2 = coordinates[i - 1][1], coordinates[i - 1][0]
            y1, x1 = coordinates[i][1], coordinates[i][0]
            current_slope = (y2 - y1)/(x2 - x1) if (x2 - x1) else float('inf')
            
            if slope is None:
                slope = current_slope
                
            elif current_slope == slope:
                slope = current_slope
                
            elif current_slope != slope:
                break
        else:
            return True
        return False
            