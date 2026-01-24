class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        permut = []
        res = []
        idx = set()

        def compute() -> None:

            if len(idx) == n:
                res.append(permut.copy())
            
            for i in range(n):

                if i not in idx:
                    permut.append(nums[i])
                    idx.add(i)
                    compute()
                    permut.pop()
                    idx.remove(i)
        
        compute()
        return res
        