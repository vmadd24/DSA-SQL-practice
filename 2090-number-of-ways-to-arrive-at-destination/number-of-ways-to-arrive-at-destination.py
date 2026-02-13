import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        
        pq = []
        heapq.heappush(pq, (0, 0))

        dist = [float('inf')]*n
        dist[0] = 0

        ways = [0]*n
        ways[0] = 1

        while pq:

            cost, u = heapq.heappop(pq)
            
            if cost > dist[n-1]:
                break

            if cost > dist[u]:
                continue
            
            for v, w in graph[u]:
                
                if dist[v] > dist[u]+w:
                    dist[v] = dist[u]+w
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v))
                    continue
                
                if dist[v] == dist[u]+w:
                    ways[v] += ways[u]
                
            
        return ways[n-1]%(10**9+7)





