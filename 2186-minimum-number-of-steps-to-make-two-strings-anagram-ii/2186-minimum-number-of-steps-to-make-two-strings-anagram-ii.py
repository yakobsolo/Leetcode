class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        ans = 0
        visted = set()
        for n in t:
            if n not in s_count:
                ans+=1
            else:
                if  n not in visted:
                    ans += max(t_count[n]-s_count[n], 0)
                    visted.add(n)
        visted =set()
        for n in s:
            if n not in t_count:
                ans+=1
            else:
                if n not in visted:
                    ans+=max(s_count[n]-t_count[n], 0)
                    visted.add(n)
                
        return ans