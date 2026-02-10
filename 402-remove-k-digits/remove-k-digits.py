class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
          
        stack = []
        ans = ""

        for c in num:
            while k > 0 and stack and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)

        while k:
            stack.pop()
            k -= 1
        
        for c in stack:
            if c == "0" and ans == "":
                continue
            ans = ans + c
        
        return ans if ans else "0"

        

        
            