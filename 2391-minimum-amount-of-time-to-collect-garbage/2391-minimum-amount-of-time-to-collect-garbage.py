class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        pcnt , mcnt, gcnt = 0, 0, 0
        pf, mf, gf  = 1, 1, 1
        tot = sum(travel)
        for i in range(n-1, -1, -1):
            pcnt += garbage[i].count("P")
            mcnt += garbage[i].count("M")
            gcnt += garbage[i].count("G")
            if "P" in garbage[i] and pf and i>0:
                pcnt += tot
                pf = 0
                
            if "M" in garbage[i] and mf and i>0:
                mcnt += tot
                mf = 0
                
            if "G" in garbage[i] and gf and i>0:
                gcnt += tot
                gf = 0
                
            tot -= travel[i-1]
            
            
                
        return gcnt + mcnt +pcnt
            
            