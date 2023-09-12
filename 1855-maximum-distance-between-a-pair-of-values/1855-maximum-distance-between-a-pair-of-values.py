class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n2 = len(nums2)
        n1 = len(nums1)
        print(n2, n1)
        max_dis = 0
        for j in range(n2-1, -1, -1):
            l  = 0
            r = n1-1 if j>n1-1 else j

            k = r
            # print(r, j, n1)
            while l<r:
                mid = l + (r-l)//2
                # print(mid, r,j)
                if nums2[j] >= nums1[mid]:
                    r = mid
                else:
                    l = mid +1
            max_dis = max(max_dis, j-r if nums2[j]>=nums1[r] else 0)
           
        return max_dis
            