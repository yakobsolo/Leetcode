class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        maxx = max(arr)
        return arr.index(maxx)
            
            