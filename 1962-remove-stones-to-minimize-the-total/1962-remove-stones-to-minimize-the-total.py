class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        import heapq
        for p in piles:
            heappush(heap, -p)
        while k:
            top = heappop(heap)
            heappush(heap, top//2)
            k-=1
        return -sum(heap)