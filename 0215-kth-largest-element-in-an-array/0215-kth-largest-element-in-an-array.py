class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for n in nums:
            if len(heap) < k:
                heappush(heap, n)
            elif n > heap[0]:
                heappop(heap)
                heappush(heap, n)
        return heap[0]