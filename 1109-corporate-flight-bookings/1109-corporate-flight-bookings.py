class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for f, e, s in bookings:
            ans[f-1]+=s
            ans[e]-=s
        for i in range(1, n):
            ans[i]+=ans[i-1]
        return ans[:-1]
        
        