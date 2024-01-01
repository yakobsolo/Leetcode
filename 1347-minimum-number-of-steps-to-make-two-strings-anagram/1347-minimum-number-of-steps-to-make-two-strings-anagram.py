class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        
        c = 0
        for k, v in t_count.items():
            if k in s_count:
                if t_count[k]>s_count[k]:
                    c += t_count[k]-s_count[k]
            else:
                c+=t_count[k]
        return c