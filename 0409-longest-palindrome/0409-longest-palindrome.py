class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        cnt = Counter(s)
        one = True
        res = 0
        for c in cnt:
            
            if cnt[c] %2 == 0: res += cnt[c]
            elif cnt[c] %2 != 0:
                if one:
                    res+=cnt[c]
                    one = False
                else: res += cnt[c] -1
        return res
        
        