class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            count = 0
            temp = strs[i]
            j = 0
            while j < len(temp) and j < len(prefix):
                if temp[j] == prefix[j]:
                    count +=1
                j+=1
                if j!= count:
                    break
            if count == 0:
                return ""
            prefix = prefix[: count]
        return prefix
                