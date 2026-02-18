class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasibility(speed: int):
            hours = 0
            for pile in piles:
                hours += (pile+speed-1)//speed
            return hours <= h

        l = 1
        r = max(piles)

        while(l<r):

            m = (l+r)//2

            if feasibility(m):
                r = m
            
            else:
                l = m+1
        
        return l
