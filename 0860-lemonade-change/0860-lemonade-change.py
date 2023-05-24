class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0 , 0
        for n in bills:
            if n == 5:
                fives +=1
                pass
            if n == 10:
                fives -=1
                tens +=1
                if fives < 0: return False
                
                pass
            if n== 20:
                
                tens -=1
                if tens < 0:
                    fives -=3
                    if fives <0: return False
                    tens+=1
                else:
                    fives -=1
                    if fives < 0: return False
        return True