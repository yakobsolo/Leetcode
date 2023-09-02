class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = defaultdict(int)
        max_long = 0
        l = 0
        n = len(s)
        max_char = 0
        for right in range(n):
            hash[s[right]] +=1
            max_char = max(max_char, hash[s[right]])
            
            while right-l+1 - max_char > k:
                hash[s[l]] -=1
                l +=1
                max_char = 0
                for key in hash:
                    max_char = max(max_char, hash[key])
                
                
                    
                
            max_long = max(right - l +1, max_long)
        return max_long