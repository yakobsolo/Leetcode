class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        ans.append(0)
        for i in range(1, n+1):
            ptr = i//2

            if i % 2 != 0:
                ans.append(ans[ptr] +1)
            else:
                ans.append(ans[ptr])
        return ans