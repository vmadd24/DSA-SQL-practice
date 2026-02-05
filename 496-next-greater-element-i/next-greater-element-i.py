class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        next_greater = {}
        stack = []

        for x in reversed(nums2):

            while stack and x > stack[-1]:
                stack.pop()
            
            if stack:
                next_greater[x] = stack[-1]
            
            else:
                next_greater[x] = -1
            
            stack.append(x)
        

        res = []

        for elem in nums1:
            res.append(next_greater[elem])
        
        return res
