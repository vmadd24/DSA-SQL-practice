class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        path = []

        def helper(pos: int, j: int) -> None:

            if j == k:
                res.append(path.copy())
            
            for i in range(1,n+1):

                if i <= pos:
                    continue
                
                path.append(i)
                helper(i, j+1)
                path.pop()
        
        helper(0, 0)

        return res