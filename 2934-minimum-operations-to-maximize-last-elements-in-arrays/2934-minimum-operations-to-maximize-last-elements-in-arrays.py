class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums2)
        def checker(nums1, nums2):
            swaps = 0
            for i in range(N-1):
                if nums1[i]>nums1[-1] or nums2[i]>nums2[-1]:
                    nums1[i], nums2[i] = nums2[i], nums1[i]
                    swaps+=1

                if nums1[i]>nums1[-1] or nums2[i]>nums2[-1]: return inf
            return swaps
        ans = checker(nums1[:], nums2[:])
        nums1[N-1], nums2[N-1] = nums2[N-1], nums1[N-1]
        ans = min(ans, checker(nums1[:], nums2[:])+1)
        
        if  ans == inf: return -1
        return ans