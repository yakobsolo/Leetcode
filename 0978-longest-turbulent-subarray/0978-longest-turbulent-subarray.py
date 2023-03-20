class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        less = 1
        greater = 1
        
        maxlong = 1
        
        for i in range(1, len(arr)):
            
            if arr[i-1] < arr[i]:
                less = greater +1
                greater = 1
            elif arr[i-1] > arr[i]:
                greater = less+1
                less = 1
            else:
                less , greater = 1, 1
            maxlong = max(maxlong , less, greater)
        return maxlong
            
            
            