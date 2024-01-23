class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onerow, onecol, zerorow, zerocol = [],[],[],[]
        N = len(grid)
        for row in grid:
            onerow.append(row.count(1))
            zerorow.append(row.count(0))
        for col in zip(*grid):
            onecol.append(col.count(1))
            zerocol.append(col.count(0))
        # print(onerow, onecol, zerorow, zerocol)
        ans = [[0]*len(grid[0]) for _ in range(N)]
        for i in range(N):
            for j in range(len(grid[0])):
                # print(i, j)
                ans[i][j]= onerow[i]+onecol[j]-zerorow[i]-zerocol[j]
                # print(ans)

        return ans