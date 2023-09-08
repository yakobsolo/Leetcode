class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        N1  = len(nums1)
        N2 = len(nums2)
        max_diff = 0
        
         
        def checker(length):
            
            subArrays = set(tuple(nums1[p1:p1+length]) for p1 in range(N1-length + 1))
            # print(subArrays)
            return any(tuple(nums2[p2:p2+length]) in subArrays for p2 in range(N2-length +1)  )          
            
        
        l, r =  0 , N1
        
        while l<=r:
            mid = l+ (r-l)//2
            # print(mid, "mid")
            
            if checker(mid):
                # print(mid)
                l = mid+1
            else:
                r = mid -1
            
        return r

        