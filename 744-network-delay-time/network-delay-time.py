import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range (1,n+1)}

        for u, v, t in times:
            graph[u].append((v, t))
        
        delay = [float('inf')]*(n)

        pq = []

        heapq.heappush(pq, (0, k))
        delay[k-1] = 0
        pop_count = 0

        while pq:

            d, u = heapq.heappop(pq)

            if d > delay[u-1]:
                continue
            
            pop_count += 1
            
            if pop_count == n:
                return d
            
            for v, t in graph[u]:
                if delay[v-1] > delay[u-1] + t:
                    delay[v-1] = delay[u-1] + t
                    heapq.heappush(pq, (delay[v-1], v))
        
        return -1

