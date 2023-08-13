class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        
        ans = [0]*n  
        for i in range(n):
            l, r = 0, n-1
            idx, mins = -1, inf
            interval = intervals[i]
            while l<=r:
                mid = l + ( r-l)//2
                if intervals[mid][0] >= interval[1] and intervals[mid][0] < mins:
                    mins = intervals[mid][0]
                    idx = intervals[mid][2]
                    r = mid-1
                else:
                    l = mid+1
            ans[intervals[i][2]] = idx
        return ans
            
            