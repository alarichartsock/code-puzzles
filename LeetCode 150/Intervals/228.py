class Solution:
    def strRange(self, start, end):
        if start == end:
            return str(start)
        else:
            return f'{start}->{end}'

    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0

        if len(nums) == 0:
            return None

        start = nums[0]
        ranges = []
        end = None
        while (i < len(nums)):
            if i == len(nums) - 1 or (nums[i] + 1 != nums[i+1]):
                end = nums[i]
                ranges.append(self.strRange(start,end))
                if i < len(nums)-1:
                    start = nums[i+1]
            if i == len(nums) - 1:
                return ranges
            i += 1
        return ranges