class Solution:
    def bin(self, nums, low=None, high=None):
        if low is None and high is None:
            low,high = 0, len(nums)-1

        if len(nums[low:high+1]) <= 3:
            return low + nums[low:high+1].index(max(nums[low:high+1]))

        idx = (low + high) // 2

        if nums[idx-1] < nums[idx] > nums[idx+1]:
            return idx
        elif nums[idx-1] < nums[idx] < nums[idx+1]:
            return self.bin(nums, idx+1, high)
        else:
            return self.bin(nums, low, idx-1)


    def findPeakElement(self, nums: List[int]) -> int:
        return self.bin(nums)