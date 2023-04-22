class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
        k = 0
        rsh = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(temp[k])
                k+=1
            rsh.append(row)
        return rsh