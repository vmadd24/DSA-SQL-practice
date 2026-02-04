class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        if n < 3:
            return []

        nums.sort()
        res = []


        for i in range(n-2):

            if (i > 0) and nums[i] == nums[i-1]:
                continue
            
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue 
            
            l, r = i + 1, n - 1
            target = (-1)*nums[i]

            while (l < r):

                if nums[l] + nums[r] < target:
                    l += 1
                
                elif nums[l] + nums[r] > target:
                    r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    
                    while (l < r and nums[l] == nums[r+1]):
                        r -= 1

        return res
        
        