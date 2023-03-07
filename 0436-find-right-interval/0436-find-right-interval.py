class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        leng= len(intervals)
        index = Counter()
        starts = []
        for i in range(leng):
            index[intervals[i][0]] = i
            starts.append(intervals[i][0])
        
        starts.sort()
        ans = []
        for j in range(leng):
            
            l=0
            h = leng-1
            starti = intervals[j][1]
            minstart = inf

            while l<=h:
                mid = (l+h)//2
                print(mid)
                if starts[mid] >= starti:
                    minstart = min(minstart, starts[mid])
                    h = mid-1
                else:
                    l= mid+1
            if minstart == inf:
                ans.append(-1)
            else:
                ans.append(index[minstart])
        
        return ans