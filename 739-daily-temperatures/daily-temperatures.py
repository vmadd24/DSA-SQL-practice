class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                answer[top] = i - top
            
            stack.append(i)

        return answer
