class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fb, fs, sb, ss = -inf, 0, -inf, 0
        
        for price in prices:
            fb = max(fb, -price)
            fs = max(fs, fb+price)
            sb = max(sb, fs-price)
            ss = max(ss, sb+price)
        return ss
        