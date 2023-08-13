class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l , r= 0, n-1
        while l<=n:
            mid  = l + (r-l)//2
            print(mid)
            if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                l = mid+1  
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
                r = mid-1
            elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            else:
                if arr[l]>arr[r]: return l
                else: return r

            