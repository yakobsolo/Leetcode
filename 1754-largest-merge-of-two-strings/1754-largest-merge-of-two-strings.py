class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
#         A = list(word1)
#         B = list(word2)

#         res = []

#         while A and B:
#             if A > B:
#                 res.append(A[0])
#                 A.pop(0)
#             else:
#                 res.append(B[0])
#                 B.pop(0)

#         return "".join(res + A + B)
       
        word1=list(word1)
        word2=list(word2)
        res = []
        
        
        while word1 and word2:
            if word1[0] > word2[0]:
                res.append(word1[0])
                word1.pop(0)
            elif word2[0] > word1[0]:
                res.append(word2[0])
                word2.pop(0)
            else:
                if word1[1:]>word2[1:]:
                    res.append(word1[0])
                    word1.pop(0)
                else:
                    res.append(word2[0])
                    word2.pop(0)
                    
            
        if word1 and not word2:
            res+=word1
        if word2 and not word1:
            res+=word2
            
        return "".join(res)
        