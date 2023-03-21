class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter_t = Counter(t)
        set_t = set(t)
        set_s = set()
        counter_s = Counter()
        
        l = 0 
        r = 0
        n = len(s)
        ans = []
        while r < n:
            
            counter_s[s[r]] +=1 
            if counter_s[s[r]] == counter_t[s[r]]:
                set_s.add(s[r])


            while len(set_s) == len(set_t):
                if ans:
                    if r-l+1 < (ans[0][1] - ans[0][0] +1):

                        ans.pop()
                        ans.append([l, r])
                else:
                    ans.append([l, r])


                if s[l] in set_t:
                    counter_s[s[l]] -=1
                    if counter_s[s[l]] < counter_t[s[l]]:
                        set_s.remove(s[l])

                l+=1
            r+=1
        if not ans:
            return ""
        
        return s[ans[0][0] :ans[0][1] +1]
           
        