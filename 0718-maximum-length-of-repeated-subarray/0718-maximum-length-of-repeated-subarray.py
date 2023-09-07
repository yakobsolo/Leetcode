class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        def checker(arr1, arr2):
            n = len(arr1)
            m = len(arr2)

            max_count = 0
            for i in range(n):

                j = 0
                while j < m:
                    k = i
                    count = 0
                    # print(i, j)
                    while k<n and j< m and arr1[k] == arr2[j]:
                        k+=1
                        count += 1
                        max_count = max(max_count, count)
                        j += 1

                    if j< m and arr1[i] != arr2[j]:
                        j+=1

            return max_count
        
        if len(nums1) == len(nums2):
            
            return max(checker(nums1, nums2), checker(nums2, nums1))
        else:
            return checker(nums1, nums2)