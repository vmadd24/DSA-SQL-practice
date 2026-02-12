import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        
        dist = [[sys.maxsize]*(k+2) for _ in range(n)]

        pq = []
        
        dist[src][0] = 0
        heapq.heappush(pq, (0, 0, src))
        
        
        while pq:

            cost, stops, city = heapq.heappop(pq)

            if cost > dist[city][stops]:
                continue
            
            if city == dst:
                return cost
            
            for v, w in graph[city]:
                if stops <= k and dist[v][stops+1] > cost + w:
                    dist[v][stops+1] = cost + w
                    heapq.heappush(pq, (dist[v][stops+1], stops+1, v))
        

        return -1
