class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        fcount, tcount = 0, 0
        maxcount= 0
        n = len(answerKey)
        l = 0
        t = k
        for i in range(n):
            if answerKey[i] == 'T': tcount+=1
            elif answerKey[i] == 'F': fcount+=1
            while tcount >k and fcount > k:
                if answerKey[l] == "T": tcount-=1
                else: fcount-=1
                l+=1
            maxcount = max(maxcount, tcount+fcount)
        
        return maxcount    
            