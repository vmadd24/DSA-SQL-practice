class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        dictn = {}

        for num in nums:
            freq = dictn.get(num, 0)
            if not freq:
                dictn[num] = 1
            else:
                dictn[num] = freq + 1

        elem_list = []

        for key in dictn.keys():

            if dictn[key] > n//3:
                elem_list.append(key)
        
        return elem_list
        
