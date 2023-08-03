class Solution:
    def minimumMoves(self, s: str) -> int:
        i, count, n = 0, 0, len(s)
        while i < n:
            if s[i] == "X":
                count +=1
                i+=3
            else:i +=1
        return count
        