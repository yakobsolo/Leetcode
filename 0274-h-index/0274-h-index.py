class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = 0
        r = len(citations)-1
        n = len(citations)
        
        if max(citations) == 0:
            return 0
        
        while l < r:
            mid = l +(r-l)//2
            
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid
        
        return n - r