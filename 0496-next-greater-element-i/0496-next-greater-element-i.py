class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreater = {}
        stack = []
        n = len(nums2)
        for i in range(n):
            
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                nextgreater[nums2[top]] = nums2[i]

            stack.append(i)
        n = len(nums1)
        res = [-1 for i in range(n)]
        for i in range(n):
            if nums1[i] in nextgreater:
                res[i] = nextgreater[nums1[i]]
        return res
                