class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas): return -1
        
        N= len(gas)
        diff  = 0
        start_idx = 0
        for i in range(N):
            diff += gas[i]-cost[i]
            if diff<0:
                diff = 0
                start_idx = i+1
        return start_idx
                