class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l,r = 0, len(arr) -1
        while l < len(arr) -1:
            if arr[l] == 0:
                arr.pop()
                arr.insert(l+1, 0)
                l+=2
            else:
                l+=1
            
        return arr