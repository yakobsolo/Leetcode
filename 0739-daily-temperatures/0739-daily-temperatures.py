class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, nextwarmer = [] , [0]*len(temperatures)
        n = len(temperatures)
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                nextwarmer[top] = i-top
            stack.append(i)
        return nextwarmer
        