class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        prev = None
        cnt = 0

        for i,num in enumerate(nums):
            if prev == num: # Duplicate encountered
                cnt += 1
            else:
                cnt = 0
            
            if prev == num and cnt >= 2: # Duplicate greater than two time encountered
                pass
            else: # Non-duplicate encountered, assign to list
                nums[idx] = num
                idx += 1
            prev = num
        return idx