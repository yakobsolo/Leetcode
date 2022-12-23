class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        stg = ""
        count = 0
        for i in range(len(s)):
            stg += s[i]
            if len(stg) >= 3:
                temp = ""
                for i in range(len(stg)):
                    if stg[i] not in temp:
                        temp += stg[i]
                if len(temp) == 3:
                    count+=1
                stg = stg[1:]
        return count
        