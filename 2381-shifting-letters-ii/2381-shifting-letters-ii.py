class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        leng = len(s)+1
        prefix = [0]*leng
        s = list(s)
        for shift in shifts:
            if shift[-1] == 0:
                prefix[shift[0]] -=1
                prefix[shift[1]+1] +=1
            else:
                prefix[shift[0]] +=1
                prefix[shift[1]+1] -=1
        prefix = list(accumulate(prefix))
        
        for i in range(leng-1):
            lett = chr((ord(s[i]) - ord('a') + prefix[i])%26 + 97)
            s[i] = lett
        
        return "".join(s)
        
            
            
          
        
            
        