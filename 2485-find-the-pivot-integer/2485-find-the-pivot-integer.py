class Solution:
    def pivotInteger(self, n: int) -> int:
        suml = 1
        sumr = n
        num = n
        if n ==1 :
            return n
        for l in range(2, n):
            
            
            
            
            
                
            if sumr> suml:
                suml += l
            if sumr == suml and l == num:
                return l
            if suml >= sumr:
                num = num -1
                sumr += num
            
            
            
            # 2 3 4 5 6 7  
            # l 15  
            # r 21
            # l 6
            # num 6
        return -1        
            
            
            
            