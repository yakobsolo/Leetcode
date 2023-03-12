class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = -1
        r = len(citations)
        n = len(citations)
        
        if max(citations) == 0:
            return 0
        
        while l + 1 < r:
            mid = l + (r - l)//2
            
            if citations[mid] < n - mid:
                l = mid
            else:
                r = mid
        
        return n - r