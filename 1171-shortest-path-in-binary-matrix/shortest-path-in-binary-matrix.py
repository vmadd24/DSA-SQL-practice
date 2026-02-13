from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)

        q = deque([(0,0,1)])

        while q:

            r, c, l = q.popleft()

            if r == n-1 and c == n-1:
                return l
            
            for dr in [-1, 0, 1]:
                for dc in [-1, 0 , 1]:

                    if dr == 0 and dc == 0: continue

                    nr, nc = r+dr, c+dc

                    if 0<=nr<n and 0<=nc<n and not grid[nr][nc]:
                        grid[nr][nc] = 1
                        q.append((nr, nc, l+1))
        
        return -1