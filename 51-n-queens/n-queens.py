class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        column = [False]*n
        diagonal = [False]*(2*n-1)
        off_diagonal = [False]*(2*n-1)

        res = []
        path = []

        def helper(row: int) -> None:

            if row == n:
                res.append(path.copy())
                return
            
            for i in range(n):

                if column[i] or diagonal[n-(row-i)-1] or off_diagonal[row+i]:
                    continue
                
                column[i] = True
                diagonal[n-(row-i)-1] = True
                off_diagonal[row+i] = True
                path.append("."*i+"Q"+"."*(n-i-1))

                helper(row+1)

                column[i] = False
                diagonal[n-(row-i)-1] = False
                off_diagonal[row+i] = False
                path.pop()
        
        helper(0)
        return res

