class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        rowleng = len(grid)
        colleng = len(grid[0])
        
        for r in range(rowleng):
            for c in range(colleng):
                if grid[r][c]:
                    peri+=4
                    if r>0 and grid[r-1][c]:
                        peri-=2
                    if c>0 and grid[r][c-1]:
                        peri-=2
        return peri