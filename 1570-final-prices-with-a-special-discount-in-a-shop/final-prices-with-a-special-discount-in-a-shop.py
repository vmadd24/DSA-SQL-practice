class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        answer = prices.copy()
        stack = []

        for i, x in enumerate(prices):

            while stack and x <= prices[stack[-1]]:
                answer[stack.pop()] -= x
            
            stack.append(i)
        
        return answer