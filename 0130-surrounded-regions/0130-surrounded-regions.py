class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        rowleng = len(board)
        colleng = len(board[0])
        
        def dfs(r, c):
            if not (0<= r< rowleng and 0<= c< colleng): return            
            if board[r][c] == "X" or board[r][c] == "1":
                return
            
            if board[r][c] == "O":
                print("yes")
                board[r][c] = "1"

            for i in range(4): 
                dfs(r+dl[i], c + dr[i])
                
        for i in range(colleng):
            dfs(0, i)
            dfs(rowleng-1, i)
                
        for i in range(rowleng):
            dfs(i, 0)
            dfs(i, colleng-1)
        
        for r in range(rowleng):
            for c in range(colleng):

                if board[r][c] == "1": board[r][c] = "O"
                elif board[r][c] == "O": board[r][c] = "X"
                    
