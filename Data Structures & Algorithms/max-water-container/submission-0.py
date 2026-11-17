class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,h = 0, len(heights)-1
        area = 0
        while l<=h:
            area = max(area, (h-l)* min(heights[l], heights[h]))
            if heights[l]> heights[h]:
                h-=1
            else:
                l+=1
        return area