class Solution:
    def distMoney(self, money: int, children: int) -> int:
        count = 0
        if children>money: return -1
        while children and money >= 8+children-1:
            count+=1
            money-=8
            children-=1
        if (children == 1 and money == 4) or (not children and money): return count-1
        return count
        
       