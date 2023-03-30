class Solution:
    def findComplement(self, num: int) -> int:
        bitt = num.bit_length()
        
        for i in  range(bitt):
            num ^=(1<<i)
        return num
            