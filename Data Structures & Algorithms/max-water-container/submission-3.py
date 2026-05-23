class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            maxArea = max(maxArea, area)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea