class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash  = defaultdict(int)
        count = 0
        n = len(s)
        l = 0
        for i, c in enumerate(s):
            hash[c] +=1
            while len(hash)>= 3:
                count += n - i
                hash[s[l]] -=1
                if hash[s[l]] == 0:
                    del hash[s[l]]
                l+=1
                
        return count
                
            
        
#         N = len(s)
#         prev = 0
#         ans = 0
#         indexes = {'a': -1, 'b': -1, 'c': -1}
#         for i, ch in enumerate(s):
#             prev += 1
#             min_idx = min(indexes.values())
#             if min_idx != -1 and s[min_idx] == ch:
#                 prev -= i - min_idx + 1
#                 print(prev)
#                 ans += prev + N - i
#             indexes[ch] = i
        
#         return ans