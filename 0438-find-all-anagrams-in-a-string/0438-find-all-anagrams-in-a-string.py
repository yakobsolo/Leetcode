class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        lenp = len(p)-1
        window_count = Counter(s[:lenp])
        lens= len(s)
        res = []
        for i in range(lenp, lens):
            window_count[s[i]] = window_count.get(s[i], 0) + 1
            if window_count == p_count:
                res.append(i - lenp)
            window_count[s[i - lenp]] -=1
            if window_count[s[i - lenp]] == 0:
                del window_count[s[i - lenp]]
        return res