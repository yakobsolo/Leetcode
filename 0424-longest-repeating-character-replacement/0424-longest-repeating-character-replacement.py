class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        hash = defaultdict(int)
        
        n = len(s)
        l = 0
        max_long = 0
        for r in range(n):
            hash[s[r]] +=1
            max_count = max(max_count, hash[s[r]])
            
            while r-l+1 - max_count >k:
                hash[s[l]] -=1
                l +=1
            
            max_long = max(max_long, r-l+1)
        return max_long