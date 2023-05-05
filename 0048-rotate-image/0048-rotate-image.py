class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for i in range(r):
                matrix[r][i] , matrix[i][r] = matrix[i][r] , matrix[r][i]
        for row in matrix:
            row[::] = row[::-1]
            