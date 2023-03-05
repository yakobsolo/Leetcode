class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = 0
        for trip in trips:
            maxx = max(maxx, trip[1],trip[-1])
        prefix = [0]*(maxx+1)
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[-1]] -= trip[0]
        prefix = list(accumulate(prefix))
        
        high = max(prefix)
        if high> capacity:
            return False
        else:
            return True
            