class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i,num in enumerate(nums):
            if num in d:
                if abs(d[num] - i) <= k:
                    return True
                else:
                    d[num] = i
            else:
                d[num] = i
        
        return False