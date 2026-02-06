class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n
        stack = []

        for i in range(n*2):

            elem = nums[i%n]
            
            while stack and elem > nums[stack[-1]]:
                ans[stack.pop()] = elem
            
            stack.append(i%n)
        
        return ans