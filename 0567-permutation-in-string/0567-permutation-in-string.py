class Solution:
            
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win1 = []
        win2 = []
        s1len = len(s1)
        s2len = len(s2)
        
        if s1len>s2len:
            return False
        win1 , win2 = [0]*26, [0]*26
        for i in range(s1len):
            win1[ord(s1[i]) - ord('a')] +=1
            win2[ord(s2[i]) - ord('a')] +=1
           
        l = 0
        r = s1len -1
   
        while r < s2len:
            if win1 == win2:
                return True
            r+=1
            if r!= s2len:
                win2[ord(s2[r]) - ord('a')] +=1
            win2[ord(s2[l]) - ord('a')] -=1
            l+=1
        return False