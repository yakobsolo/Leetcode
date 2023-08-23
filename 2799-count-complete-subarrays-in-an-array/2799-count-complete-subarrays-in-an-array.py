class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        init = set(nums)
        count,i = 0 ,0
        window = defaultdict(int) #hash map 

        for j in nums : 
            window[j] += 1
            while len(window) == len(init):
                if window[nums[i]] == 1 :
                    window.pop(nums[i])
                else : 
                    window[nums[i]] -= 1
                i += 1
            count += i
        return count
                