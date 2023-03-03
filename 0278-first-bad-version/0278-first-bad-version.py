# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        bad = []
        while low <= high:
            mid = (low+high)//2
            if not isBadVersion(mid):
                low = mid +1
            elif isBadVersion(mid):
                bad.append(mid)
                high = mid -1
        
        if bad:
            bad.sort()
            return bad[0]
        return None
                
            
        
        