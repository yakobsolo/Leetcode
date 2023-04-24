class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0,0
        ans = []
        flag = 1
        while i < len(word1) and j < len(word2):
            if flag:
                ans.append(word1[i])
                i +=1
                flag = 0
            else:
                ans.append(word2[j])
                j+=1
                flag = 1
        
        if i<len(word1):
            ans.append(word1[i:])
        if j< len(word2):
            ans.append(word2[j:])
        return "".join(ans)
        