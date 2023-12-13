class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ['1']
        i = 0
        N = len(pattern)
        cur = 1
        while i < N:
            if pattern[i] == "I":
                cur +=1
                ans.append(str(cur))
                i+=1
            else:
                count = 1
                i+=1
                while i<N and pattern[i] == "D":
                    count+=1
                    i+=1
                
                top = ans.pop()
                start = int(top)+count
                cur=start
                for k in range(count+1):
                    ans.append(str(start))
            
                    start-=1
                
            
        return "".join(ans)
                    
                
                