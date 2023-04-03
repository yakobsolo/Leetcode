class Solution:
    def countArrangement(self, N):
        self.visted = 0
        self.count = 0
        def permutation(idx):
            if (idx,self.visted) not in memo:
                if self.visted.bit_count() == N:
                    # for i in range(len(perm)):
                    #     if ((perm[i] % (i+1) != 0) and ((i+1) % perm[i] != 0)):
                    #         return 
                    # self.count +=1
                    return 1
                
                count = 0
                for i in range(N):
                    if not (self.visted & (1<<i)):
                        if (i+1)% idx == 0 or idx%(i +1) == 0:

                            self.visted |= (1<<i)
                            count += permutation( idx+1)
                            self.visted &= ~(1<<i)
                            
                memo[(idx,self.visted)] = count
                
            return memo[(idx,self.visted)]
        
        memo = {}
        return permutation( 1)
        # return self.count