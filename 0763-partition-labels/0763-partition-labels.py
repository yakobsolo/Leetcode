class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        i = 0
        temp =[]
        while i < len(s):
            
            temp.append(s[i])
            j = len(temp)-1
            while j>=0 and temp and i+1< len(s) and temp[j] not in s[i+1:]:
                j-=1
            if j < 0:
                ans.append(len(temp))
                temp = []
            i+=1
        if temp:
            ans.append(len(temp))
        return ans
                           