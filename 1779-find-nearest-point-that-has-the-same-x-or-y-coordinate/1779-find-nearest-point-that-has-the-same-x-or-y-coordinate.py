class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minman = inf
        hash = [minman, -1]
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                minn = abs(x - points[i][0]) + abs(y- points[i][1])
                if minn < minman:
                    
                    minman = min(minman, minn)
                    hash = [minman, i]
        return hash[1]