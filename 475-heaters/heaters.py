class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        n = len(heaters)
        
        ans = 0

        def search_nearest(x: int) -> int:

            nonlocal n

            l = 0
            r = n-1

            while l+1<r:

                mid = (l+r)//2

                if x < heaters[mid]:
                    r = mid
                
                elif x > heaters[mid]:
                    l = mid
                
                else:
                    return heaters[mid]
            
            if abs(heaters[l]-x) < abs(heaters[r]-x):
                return heaters[l]
            
            return heaters[r]


        for i in houses:
            ans = max(ans, abs(i - search_nearest(i)))
        
        return ans
        


        
