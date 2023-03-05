class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i, h in enumerate(heights):
            # Before adding a new building pop the building who is taller than the new one.
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans
