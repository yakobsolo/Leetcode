class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for r in matrix:
            for c in r:
                heappush(heap, c)
        for _ in range(k):
            sml = heappop(heap)
        return sml