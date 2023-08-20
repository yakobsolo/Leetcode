class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = []
        for n in nums1:
            if n not in arr and (n in nums2 or n in nums3):
                arr.append(n)
        
        for n in nums2:
            if n not in arr and (n in nums1 or n in nums3):
                arr.append(n)
        for n in nums3:
            if n not in arr and (n in nums1 or n in nums2):
                arr.append(n)
        return arr