class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for i in range(len(nums)):
            heappush(heap, -nums[i])
        while k > 0:
            kth = heappop(heap)
            k-=1
        return -kth
            