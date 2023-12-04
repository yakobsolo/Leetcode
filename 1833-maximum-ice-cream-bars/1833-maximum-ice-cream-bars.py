class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sm = 0
        ans = 0
        for n in costs:
            sm+=n
            if sm<= coins:
                ans += 1
                
        return ans