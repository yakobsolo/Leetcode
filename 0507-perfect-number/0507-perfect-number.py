class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sm = 1
        if num==1:
            return False
    
        
        i = 2
        while i<=sqrt(num):
            if num%i == 0:
                sm += i+num//i
            i+=1
        if sm == num:
            return True
        return False