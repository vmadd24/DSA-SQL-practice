class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = 0
        s = nums[0]
        min_len = n+1

        while r < n:

            if s < target and r < n-1:
                r += 1
                s += nums[r]
            
            elif s < target and r == n-1:
                break
            
            else:
                min_len = min(min_len, r-l+1)
                s -= nums[l]
                l += 1


        return min_len if min_len != n+1 else 0