class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = 0
        s = nums[0]
        min_len = n+1

        while r < n:

            if s < target:
                r += 1
                if r < n:
                    s += nums[r]
                else:
                    break
            
            else:
                min_len = min(min_len, r-l+1)
                s -= nums[l]
                l += 1


        return min_len if min_len != n+1 else 0