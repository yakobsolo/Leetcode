class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heappush(heap, matrix[r][c])
        while k>1:
            heappop(heap)
            k-=1
        return heap[0]