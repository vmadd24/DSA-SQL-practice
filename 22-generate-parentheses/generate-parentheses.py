class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        path = []
        l = n
        r = n

        def helper(l: int, r: int) -> None:

            if l == 0 and r == 0:
                result.append("".join(path))
                return
            
            if l > 0:
                path.append("(")
                helper(l-1, r)
                path.pop()
            
            if r > 0 and r > l:
                path.append(")")
                helper(l, r-1)
                path.pop()

        path.append("(")
        helper(l-1, r)

        return result