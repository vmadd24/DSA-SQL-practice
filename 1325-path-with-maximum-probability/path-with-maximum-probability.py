import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        graph = {i: [] for i in range(n)}

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        pq = [(-1.0, start_node)]

        while pq:
            curr_p, u = heapq.heappop(pq)
            curr_p = -curr_p

            if u == end_node:
                return curr_p
            
            if curr_p < max_prob[u]:
                continue

            for v, prob in graph[u]:
                new_prob = curr_p * prob
                
                if new_prob > max_prob[v]:
                    max_prob[v] = new_prob
                    heapq.heappush(pq, (-new_prob, v))

        return 0.0

        