class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r,c = 0,0,0
        temp = nums1.copy()
        while l<m and r<n:
            if temp[l] < nums2[r]:
                nums1[c] = temp[l]
                l+=1
            else:
                nums1[c] = nums2[r]
                r +=1 
            c += 1
        while l<m:
            nums1[c] = temp[l]
            l+=1
            c+=1
        while r<n:
            nums1[c] = nums2[r]
            r+=1
            c+=1
        return nums1
            