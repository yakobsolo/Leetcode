class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums2)
        increasing = [0]
        for i in range(1, len(nums2)):
            while increasing and nums2[increasing[-1]] < nums2[i]:
                
                top = increasing.pop()
                ans[top] = nums2[i]
            increasing.append(i)
        answer =[]
        hash = {}
        for i in range(len(nums2)):
            hash[nums2[i]] = i
        for j in range(len(nums1)):
            ind = hash[nums1[j]]
            answer.append(ans[ind])
        return answer