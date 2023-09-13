class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        
        for i in range(n):
            l, r = 0 , n-1
            while l<=r:
                mid = l + (r-l)//2
                # print(l, r, mid)
                if 2*arr[mid] == arr[i] and i != mid:
                    return True
                elif 2*arr[mid] > arr[i]:
                    r = mid-1
                else:
                    l= mid +1
        return False
    
                