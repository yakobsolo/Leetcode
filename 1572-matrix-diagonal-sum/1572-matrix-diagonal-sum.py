class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        leng = len(mat)-1
        for i in range(len(mat)):
            if leng-i == i:
                sums-= mat[i][i]
            sums+= mat[i][i]
            sums+= mat[i][leng-i]
        return sums