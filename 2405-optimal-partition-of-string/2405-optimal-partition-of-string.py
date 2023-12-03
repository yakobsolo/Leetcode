class Solution:
    def partitionString(self, s: str) -> int:
        
        window = set()
        count = 0
        for c in s:
            if c not in window:
                window.add(c)
            else:
                window = set()
                window.add(c)
                count+=1
        if window:
            count+=1
        return count