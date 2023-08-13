class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        if max(citations) == 0 : return 0
        maxh = 0
        while l<r:
            mid = l +(r-l)//2
            if citations[mid] <n-mid:
                l = mid +1
            else:
                r = mid
                
        return n - r