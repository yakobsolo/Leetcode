class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <=2:
            return False
        
        def additive(index, first, second):
            if index == int(len(num)):
                return True
            k = index
            while k < len(num):
                 
                cur = int(num[index: k+1])
                if first+second == cur and additive(k+1, second, cur):
                    return True
                if cur == 0:
                    break
                k+=1
            return False
        i =0
        
        while i < len(num)-2:
            j = i+1
            flag = 0
            while j < len(num)-1:
                first = int(num[: i+1])
                second = int(num[i+1: j+1])
                
                if additive(j+1, first, second):
                    return True
                if second == 0:
                    break
                    
                j+=1
            
            if first == 0:
                return False
            i+=1
        return False