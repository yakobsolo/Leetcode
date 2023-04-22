class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowleng = len(matrix)
        colleng = len(matrix[0])
        for r in range(rowleng):
            for c in range(colleng):
                if matrix[r][c] == 0:
                    i, j = r, c
                    
                    while 0<= i< rowleng and 0<= j < colleng:
                        
                        if i!= r and matrix[i][j] != 0 and matrix[i][j] != "0":
                            matrix[i][j] = "0"
                        elif i == r:
                            matrix[i][j] = "0"
                        i -=1
                        
                    i, j = r, c
                    while 0<= i< rowleng and 0<= j < colleng:
                        
                        if i!=r and matrix[i][j] != 0 and matrix[i][j] != "0":
                            matrix[i][j] = "0"
                        elif i == r:
                            matrix[i][j] = "0"
                        i +=1
                        
                    i, j = r, c
                    while 0<= i< rowleng and 0<= j < colleng:
                        
                        if j!= c and matrix[i][j] != 0 and matrix[i][j] != "0":
                            matrix[i][j] = "0"
                        elif j == c:
                            matrix[i][j] = "0"
                        j -=1
                        
                    i, j = r, c
                    while 0<= i< rowleng and 0<= j < colleng:
                        
                        if j!= c and matrix[i][j] != 0 and matrix[i][j] != "0":
                            matrix[i][j] = "0"
                        elif j == c:
                            matrix[i][j] = "0"
                        j +=1
        for r in range(rowleng):
            for c in range(colleng):
                if matrix[r][c] == "0":
                    matrix[r][c] = 0
                    
            