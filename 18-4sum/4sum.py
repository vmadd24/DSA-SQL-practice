class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        if n < 4:
            return []

        nums.sort()
        res = []
        
        for i in range(n-3):
            
            if (i > 0) and nums[i] == nums[i-1]:
                continue
            
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            self.threeSum(i, nums, n, target - nums[i], res)
        
        return res

    

    def threeSum(self, start_idx: int, nums: List[int], n: int, target: int, res: List[int]) -> None:

        if n - start_idx - 1 < 3:
            return

        for i in range(start_idx+1, n-2):

            if (i > start_idx+1) and nums[i] == nums[i-1]:
                continue
            
            if nums[i] + nums[i+1] + nums[i+2] > target:
                break
            
            if nums[i] + nums[n-2] + nums[n-1] < target:
                continue
            
            l = i+1
            r = n-1
            sub_target = target - nums[i]

            while l < r:

                if nums[l] + nums[r] < sub_target:
                    l += 1
                
                elif nums[l] + nums[r] > sub_target:
                    r -= 1
                
                else:
                    res.append([nums[start_idx], nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    
                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1
