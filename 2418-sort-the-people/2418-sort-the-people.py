class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxx = max(heights)
        count = [-1]*(maxx +1)
        for i in range(len(heights)):
            count[heights[i]] = i
        
        ans = []
        
        for j in range(len(count) -1, -1, -1):
            if count[j] != -1:
                ans.append(names[count[j]])
        return ans