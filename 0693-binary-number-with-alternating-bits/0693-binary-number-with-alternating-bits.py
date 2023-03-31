class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n&(1)
        for i in range(1, n.bit_length()):
            if n&(1<<i) != 0:
                temp = 1
            else:
                temp = 0
           
            if temp == prev:
                return False
            prev = temp
        return True