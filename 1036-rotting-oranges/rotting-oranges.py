from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_oranges = 0
        r = len(grid)
        c = len(grid[0])

        queue_deque = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue_deque.append((i, j, 0))
        
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        minute = 0
    
        while queue_deque:
            x, y, level = queue_deque.popleft()
            minute = max(minute, level)
            
            for xpos, ypos in directions:
                xnew = x+xpos; ynew = y+ypos
                if 0 <= xnew < r and 0 <= ynew < c and grid[xnew][ynew] == 1:
                    grid[xnew][ynew] = 2
                    queue_deque.append((xnew, ynew, level+1))
                    fresh_oranges -= 1
        

        if fresh_oranges > 0:
            return -1

        else:
            return minute

            

            
    
        
