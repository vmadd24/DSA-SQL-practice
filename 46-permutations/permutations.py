class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        permut = []
        res = []
        visited = [False]*n

        def compute() -> None:

            if len(permut) == n:
                res.append(permut.copy())
            
            for i in range(n):

                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i]):
                    continue
                
                permut.append(nums[i])
                visited[i] = True
                compute()
                permut.pop()
                visited[i] = False
        
        compute()

        return res
        