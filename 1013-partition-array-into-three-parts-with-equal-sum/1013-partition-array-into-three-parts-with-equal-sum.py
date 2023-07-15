class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tot = sum(arr)
        if tot%3 != 0: return False
        
        n = len(arr)
        count , div, target = 0, 0, tot//3
        
        for i in range(n):
            div +=arr[i]
            if div == target:
                div = 0
                count +=1
        if count >= 3: return True
        else: return False
            
            