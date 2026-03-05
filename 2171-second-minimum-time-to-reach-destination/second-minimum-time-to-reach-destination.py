class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        graph = {i:[] for i in range(1,n+1)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        dist = {i: [] for i in range(1, n+1)}

        pq = []
        heapq.heappush(pq, (0, 1))

        while pq:

            t, u = heapq.heappop(pq)

            if u == n and len(dist[u]) == 2 and t == dist[u][1]:
                return t
            
            signal = (t//change)

            if signal%2:
                t = (signal+1)*change
            
            new_time = t + time
            
            for v in graph[u]:

                if not dist[v]:
                    dist[v].append(new_time)
                    heapq.heappush(pq, (new_time, v))

                elif len(dist[v]) == 1 and new_time != dist[v][0]:
                    dist[v].append(new_time)
                    heapq.heappush(pq, (new_time, v))
                
        return -1
            
            