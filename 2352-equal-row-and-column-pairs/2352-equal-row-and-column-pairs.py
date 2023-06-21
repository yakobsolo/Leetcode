class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col = []
        n  = len(grid)
        for r in range(n):
            temp = []
            for c in range(n):
                temp.append(grid[c][r])
            col.append(temp)
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == col[j]: count+=1
        return count
            
            