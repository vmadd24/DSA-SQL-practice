class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        res = []
        path = []
        l = len(graph)

        def backtrack(n: int) -> None:

            nonlocal l

            if n == l-1:
                res.append(path.copy())
                return
            
            for i in graph[n]:
                
                path.append(i)
                backtrack(i)
                path.pop()
        

        path.append(0)
        backtrack(0)
        return res
        