class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        visted = set()
        leng  = len(nums)
        count =0 
        def reversedigit(n):
            n = str(n)
            n = list(n)
            l , r = 0, len(n)-1
            while l< r:
                n[l] , n[r] = n[r], n[l]
                l+=1
                r-=1
            ans = "".join(n)
            return int(ans)
        
        for i in range(leng):
            if nums[i] not in visted:
                count +=1
            visted.add(nums[i])
            r = reversedigit(nums[i])
            if r not in visted:
                count +=1
                visted.add(r)
        return count
            