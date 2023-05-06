class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h = [-a for a in nums]
        heapify(h)
        while k!=0:
            l = heappop(h)
            k -=1
        return -l
        