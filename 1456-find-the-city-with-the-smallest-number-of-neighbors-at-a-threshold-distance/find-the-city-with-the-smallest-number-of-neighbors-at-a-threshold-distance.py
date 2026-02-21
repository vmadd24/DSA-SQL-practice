class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        dp = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0
    
        for u,v,w in edges:
            dp[u][v] = w
            dp[v][u] = w
        

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        ans = 0
        min_cities = n

        for i in range(n):
            city_count = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    city_count += 1
            if city_count <= min_cities:
                min_cities = city_count
                ans = i
        
        return ans