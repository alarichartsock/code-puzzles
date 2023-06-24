class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        prev = None

        for i,num in enumerate(nums):
            if prev == num: # Duplicate encountered
                pass
            else:
                nums[idx] = num
                idx += 1
            prev = num
        return idx