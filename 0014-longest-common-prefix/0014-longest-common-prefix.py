class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < len(minstr):
                minstr = strs[i]
        res = ""
        for i in range(len(minstr)):
            cur = strs[0][i]
            
            for j in range(1, len(strs)):
                if cur != strs[j][i]:
                    return res
            res += cur
        return res
                