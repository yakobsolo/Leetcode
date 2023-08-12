# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1 
        minn = n
        while l<=n:
            mid = l + (n-l)//2
            
            if not isBadVersion(mid):
                l = mid+1
            else:
                minn = min(minn, mid)
                n = mid-1
        return minn