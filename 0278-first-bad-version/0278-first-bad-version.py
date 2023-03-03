# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        min_bad = inf
        while low <= high:
            mid = (low+high)//2
            if not isBadVersion(mid):
                low = mid +1
            elif isBadVersion(mid):
                min_bad = min(min_bad, mid)
                high = mid -1
        
        return min_bad
                
            
        
        