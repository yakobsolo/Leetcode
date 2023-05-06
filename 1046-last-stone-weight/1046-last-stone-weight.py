class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        h = []
        for ele in stones:
            h.append(-ele)
        heapq.heapify(h)
        while len(h)>1:
            a = heappop(h)
            b = heappop(h)
            if a<b:
                heappush(h, a -b)
            
        if h:
            return -h[0]
        else:
            return 0