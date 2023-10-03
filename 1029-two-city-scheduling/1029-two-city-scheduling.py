class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key=lambda x:abs(x[0]-x[1]), reverse = True)
        res = 0
        n = len(sorted_costs)
        lengb = n//2
        lenga = n//2
        print(sorted_costs)
        for a, b in sorted_costs:
            if lenga>0 and lengb>0:
                if a<b:
                    lenga-=1
                    res += a
                else:
                    lengb-=1
                    res +=b
            elif lenga==0:
                res+=b
            else:
                res+=a
        return res