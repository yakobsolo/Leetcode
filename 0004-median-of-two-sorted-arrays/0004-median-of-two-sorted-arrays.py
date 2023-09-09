class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        n = len(nums1)
        if n%2 == 0:
            l = int(n/2 -1)
            r = int(l +1)
            return (nums1[l]+ nums1[r])/2
        else:
            mid = n//2
            return nums1[mid]
