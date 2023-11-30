class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr  = [0]*N
        
        tot = sum(nums)
        
        prefix = []
        for i in range(N):
            if prefix:
                prefix.append(prefix[-1]+nums[i])
            else: prefix.append(nums[i])
                
        print(prefix)
        for i in range(N):
            arr[i] = (i)*nums[i]-(prefix[i]-nums[i])+tot-prefix[i]-(N-i-1)*nums[i]
        return arr