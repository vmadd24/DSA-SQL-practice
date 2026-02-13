import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n = len(heights)
        m = len(heights[0])

        pq = []
        heapq.heappush(pq, (0, 0, 0))
        dist = [[float('inf')] * m for _ in range(n)]

        while pq:

            h, r , c = heapq.heappop(pq)

            if r == n-1 and c == m-1:
                return h
            
            if dist[r][c] < h:
                continue

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(h, diff)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))

        return -1



