class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        greatest = 0

        for i in range(len(heights)):
            stack = heights[i:]
            while stack:
                greatest = max(greatest, min(stack) * len(stack))
                stack.pop()
            
        return greatest