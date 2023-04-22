class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        mtx = [[0]* (n-2) for i in range(n-2)]
        
        for r in range(n-2):
            for c in range(n-2):
                mtx[r][c] = grid[r][c]
                for i in range(3):
                    for j in range(3):
                        mtx[r][c] = max(mtx[r][c] , grid[r+i][c+j])
        return mtx