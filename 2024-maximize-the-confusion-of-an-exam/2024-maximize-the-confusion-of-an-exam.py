class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        fcount, tcount = 0, 0
        maxfcount, maxtcount = 0, 0
        n = len(answerKey)
        l = 0
        t = k
        for i in range(n):
            if answerKey[i] == 'T': tcount+=1
                
            else:
                if k>0:
                    k-=1
                    tcount+=1
                else:
                    while k==0:
                        if answerKey[l] == "F":
                            k+=1
                        else: tcount-=1
                        l+=1
                    k-=1
                    
            maxtcount = max(maxtcount, tcount)
        l = 0
        k = t
        for i in range(n):
            if answerKey[i] == 'F': fcount+=1
            else:
                if k>0:
                    k-=1
                    fcount+=1
                else:
                    while k==0:
                        if answerKey[l] == "T":
                            k+=1
                        else: fcount-=1
                        l+=1
                    k-=1
                    
            # print(i, fcount, k)
            maxfcount = max(maxfcount, fcount)
        
        return max(maxtcount, maxfcount)
        
            
                
                    
                