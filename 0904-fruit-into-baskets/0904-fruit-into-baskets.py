class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, ans, total = 0, 0, 0
        counts = defaultdict(int)
        
        leng = len(fruits)
        for  r in range(leng):
            counts[fruits[r]] +=1
            total +=1 
            
            while len(counts) > 2:
                fruit = fruits[l]
                counts[fruit] -=1
                total -=1
                
                if counts[fruit] == 0:
                       del counts[fruit]
                l +=1
            ans = max(ans, total)
        return ans