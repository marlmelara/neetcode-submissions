class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water_amount = defaultdict(int)

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            water_amount[(left, right)] = area

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            elif heights[right] == heights[left]:
                left += 1
                right -= 1

        return max(water_amount.values())