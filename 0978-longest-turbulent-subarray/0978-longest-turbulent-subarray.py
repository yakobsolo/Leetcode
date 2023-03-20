class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 0
        leng = len(arr)
        maxlong = 0
        long = 0
        if leng == 1:
            return 1
        
        
        
        while r < leng:
            while (l < leng-1) and (arr[l] == arr[l+1]):
                l +=1
                
            while (r< leng-1)and ((arr[r-1] < arr[r] > arr[r+1] ) or (arr[r-1] > arr[r] < arr[r+1])):
                
                r +=1
                
            long = r - l +1
            maxlong = max(maxlong, long)
            l = r 
            r +=1
        return maxlong
            
            