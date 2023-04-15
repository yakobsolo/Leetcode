class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leng= len(matrix)
        
        for i in range(1, leng):
            if target < matrix[i][0]:
                temp = set(matrix[i-1])
                if target in temp:
                    return True
                return False
            
        if target in set(matrix[-1]):
            return True
        return False
                