class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowleng = len(matrix)
        colleng = len(matrix[0])
        row, col = set(), set()
        
        for r in range(rowleng):
            for c in range(colleng):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        for i in row:
            matrix[i] = [0]* colleng
       

        for j in col:
            for r in range(rowleng):
               
                matrix[r][j] = 0
                