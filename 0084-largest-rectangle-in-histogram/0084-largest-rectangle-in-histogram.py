class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leng = len(heights)
        prevsmaller = [-1]*leng
        nextsmaller = [leng]*leng
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                nextsmaller[top] = i
            if stack:
                prevsmaller[i] = stack[-1]
            
            stack.append(i)
        maxx = 0  
        for i in range(leng):
            width = nextsmaller[i] - prevsmaller[i] -1
            area = width*heights[i]
            maxx = max(maxx, area)
        return maxx
