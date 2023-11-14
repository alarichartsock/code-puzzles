class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []

        beat = max(candies)

        for i in candies:
            if i+extraCandies >= beat:
                ret.append(True)
            else:
                ret.append(False)
        
        return ret

#revised:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [x+extraCandies >= max(candies)for x in candies]