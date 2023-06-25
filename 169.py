from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2

        counter_obj = Counter(nums)

        for item in counter_obj.items():
            if item[1] >= n:
                return item[0]