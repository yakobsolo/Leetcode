class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        prefix = []
        
        N = len(words)
        
        v = {"a", "i", "o", "u", "e"}
        for i in range(N):
            if prefix:
                if words[i][0]  in v and words[i][-1] in v:
                    prefix.append(prefix[-1]+1)
                else:
                    prefix.append(prefix[-1])
            else:
                if words[i][0]  in v and words[i][-1] in v:
                    prefix.append(1)
                else:
                    prefix.append(0)
        prefix.append(0)
        for  l, r in queries:
            ans.append(prefix[r]-prefix[l-1])
        return ans