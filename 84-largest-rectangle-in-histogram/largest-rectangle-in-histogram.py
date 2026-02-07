class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []
        heights = heights + [0]

        for i, x in enumerate(heights):

            while stack and x < heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()]*(i-(stack[-1]+1 if stack else 0)))
            
            stack.append(i)
        
        return max_area