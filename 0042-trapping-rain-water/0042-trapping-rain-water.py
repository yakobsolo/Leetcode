class Solution:
    def trap(self, height: List[int]) -> int:
        nextgreater = []
        res = 0
        for i in range(len(height)):
            while nextgreater and nextgreater[-1][1] < height[i]:
                top = nextgreater.pop()
                if nextgreater:
                    
                    minn = min(height[i], nextgreater[-1][1]) - top[-1]
                    width = i - nextgreater[-1][0] -1
                    res += (width)*(minn)
                
            nextgreater.append([i, height[i]])
        return res
        