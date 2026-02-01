class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)

        for i, x in enumerate(nums):

            if (i > 0) and x == nums[i-1]:
                continue
            
            l, r = i + 1, n - 1
            target = (-1)*x

            while (l < r):

                if nums[l] + nums[r] < target:
                    l += 1
                
                elif nums[l] + nums[r] > target:
                    r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while(nums[l] == nums[l-1] and l < r):
                        l += 1

        return res
        
        