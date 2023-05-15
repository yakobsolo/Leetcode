class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        res = 0
        for i in range(k):
            top = heapq.heappop(heap)
            res += -top
            heapq.heappush(heap, top-1)
        return res