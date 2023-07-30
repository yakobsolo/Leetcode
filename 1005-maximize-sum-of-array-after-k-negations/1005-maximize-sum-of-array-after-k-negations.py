class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        while k:
            minn = heapq.heappop(nums)
            heapq.heappush(nums, -minn)
            k-=1
        return sum(nums)