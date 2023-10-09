class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack =  list(haystack)
        needle = list(needle)
        n, N = len(needle), len(haystack)
        for i in range(N-n+1):
            # print(haystack[i:n+i])
            if haystack[i:n+i] == needle:
                return i
        return -1