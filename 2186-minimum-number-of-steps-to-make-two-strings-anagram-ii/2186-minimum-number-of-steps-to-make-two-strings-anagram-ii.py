class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s_count = Counter(s)
        t_count = Counter(t)
        
        ans = 0
        for let in alphabet:
            ans+=abs(s_count[let]-t_count[let])
        return ans