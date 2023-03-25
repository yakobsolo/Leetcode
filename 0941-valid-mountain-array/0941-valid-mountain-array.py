class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        leng = len(arr)
        i =0
        while i < leng-1:
            if arr[i] > arr[i+1]:
                i +=1
                break
            elif arr[i] == arr[i+1]:
                return False
            i +=1
        if i == 1:
            return False
        while i < leng:
            if arr[i] >= arr[i-1]:
                return False
            i+=1
        return True