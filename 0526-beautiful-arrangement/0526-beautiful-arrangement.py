class Solution:
    def countArrangement(self, N):
        self.visted = 0
        self.count = 0
        def permutation(perm, idx):
            if self.visted.bit_count() == N:
                # for i in range(len(perm)):
                #     if ((perm[i] % (i+1) != 0) and ((i+1) % perm[i] != 0)):
                #         return 
                self.count +=1
                return
            
            for i in range(N):
                if not (self.visted & (1<<i)):
                    if (i+1)% idx == 0 or idx%(i +1) == 0:
                        
                        perm.append(i+1)
                        self.visted |= (1<<i)

                        permutation(perm, idx+1)
                        perm.pop()
                        self.visted &= ~(1<<i)
        
        permutation([], 1)
        return self.count