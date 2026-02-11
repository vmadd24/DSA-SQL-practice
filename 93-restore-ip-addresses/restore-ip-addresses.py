class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        path = []
        n = len(s)

        def backtrack(idx: int, numOfSeg: int) -> None:

            nonlocal s, n, path

            if numOfSeg == 4:
                if idx == n:
                    ans.append("".join(path.copy())[:-1])
                return

            
            for pos in range(1,4):

                if idx+pos>n:
                    return

                seg = s[idx:idx+pos]
                if isValid(seg):
                    path = path + [seg, "."]
                    backtrack(idx+pos, numOfSeg+1)
                    path.pop()
                    path.pop()
                
                if seg == "0":
                    return
        

        def isValid(seg: str) -> bool:
            return 0<=int(seg)<=255

        backtrack(0, 0)

        return ans
                


        
        
        