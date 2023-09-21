class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n , m = len(board), len(board[0])
        
        visted = set()
        def isValid(i, j):
            return (i>=0 and i<n and j>=0 and j<m) and (i,j) not in visted and board[i][j] == "X"
        def dfs(i, j):
            visted.add((i, j))
            for r, c in directions:
                r,c = i+r, j+c
                
                if isValid(r, c):
                    dfs(r, c)
                
                
        
        count = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visted and board[i][j] == "X":
                    dfs(i, j)
                    count+=1
        return count