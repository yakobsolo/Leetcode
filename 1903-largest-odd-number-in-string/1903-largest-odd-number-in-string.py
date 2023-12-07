class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = ["1" , "3", "5", "7", "9"]
        
        mx = 0
        flg = 0
        for odd in odds:
            for i in range(len(num)):
                if num[i] == odd:
                    mx = max(mx, i)
                    flg = 1
                    print(i)
        return num[:mx+1] if flg else ""
                     
            