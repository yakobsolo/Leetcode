class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = set()
        N= len(stones)
        dp.add(0)
        summ = sum(stones)
        if summ%2 == 0:
            target = (summ)//2
        else:target = (summ-1)//2
        for i in range(N):
            temp = set()
            for val in dp:
                if val+stones[i]<=target:
                    temp.add(val+stones[i])
                
                    
            dp.update(temp)
        return summ-(max(dp)*2)
