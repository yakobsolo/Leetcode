class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        nextTempreture = []
        
        for i in range(len(temperatures)):
            
            while nextTempreture and temperatures[nextTempreture[-1]] < temperatures[i]:
                top = nextTempreture.pop()
                ans[top] = i - top
            nextTempreture.append(i)
        return ans