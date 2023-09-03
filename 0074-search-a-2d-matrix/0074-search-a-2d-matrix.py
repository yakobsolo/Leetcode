class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        arr = []
        for mat in matrix:
            for n in mat:
                arr.append(n)
        
        return bisect_left(arr, target) != bisect_right(arr,target)