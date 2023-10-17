class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        a_sum, b_sum = [], []
        count = 0
        for i in range(N):
            if s[i] == "b":
                count+=1
                b_sum.append(count)
            else:
                b_sum.append(count)
        count = 0
        for j in range(N-1, -1, -1):
            if s[j] == "a":
                count +=1
                a_sum.append(count)
            else:
                a_sum.append(count)
        mn = inf
        
        a_sum = a_sum[::-1]
        # print(a_sum, b_sum)
        for i in range(N):
            mn = min(a_sum[i]+b_sum[i]-1, mn)
        return mn