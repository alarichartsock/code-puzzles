class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height) - 1
        ret = 0

        while i < j:
            water = min(height[i],height[j]) * (j - i)
            ret = max(ret, water)

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        
        return ret