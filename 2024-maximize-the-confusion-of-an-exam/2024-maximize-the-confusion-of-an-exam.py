class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        fcount, tcount = 0, 0
        maxfcount, maxtcount = 0, 0
        nums = answerKey
        n = len(answerKey)
        l = 0
        t = k
        for i in range(n):
            if nums[i] == 'T': tcount+=1
                
            else:
                if k>0:
                    k-=1
                    tcount+=1
                else:
                    while k==0:
                        if nums[l] == "F":
                            k+=1
                        else: tcount-=1
                        l+=1
                    k-=1
                    
            maxfcount = max(maxfcount, tcount)
        l = 0
        k = t
        for i in range(n):
            if nums[i] == 'F': fcount+=1
            else:
                if k>0:
                    k-=1
                    fcount+=1
                else:
                    while k==0:
                        if nums[l] == "T":
                            k+=1
                        else: fcount-=1
                        l+=1
                    k-=1
                    
            # print(i, fcount, k)
            maxtcount = max(maxtcount, fcount)
        
        return max(maxtcount, maxfcount)
        
            
                
                    
                