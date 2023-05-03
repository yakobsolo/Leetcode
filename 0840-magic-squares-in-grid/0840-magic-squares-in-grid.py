class Solution:
    def numMagicSquaresInside(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])
        count = 0
        g = set(range(1, 10))
        
        print(sum(G, []))
        for i in range(m-2):
            for j in range(n-2):
                mgc = []
                for k in range(3):
                    mgc += [G[i+k][j:j+3]]
                if set(sum(mgc,[])) != g or mgc[1][1] != 5: continue
                if any(sum(mgc[k]) != 15 for k in range(3)) or any(sum([mgc[k][l] for k in range(3)]) != 15 for l in range(3)): continue
                if sum([mgc[k][k] for k in range(3)]) != 15 or sum([mgc[k][2 -k] for k in range(3)]) != 15: continue
                count +=1
        return count
    
    