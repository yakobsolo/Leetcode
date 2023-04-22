class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if 0<= x<10:
            return True
        
        r = 0
        n = x

        if x%10 == 0:
            return False
        else:
            while x>=1:
                r = r*10 + x%10
                x //= 10
        if r == n:
            return True
        return False