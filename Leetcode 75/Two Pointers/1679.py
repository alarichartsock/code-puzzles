class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j,ret = 0, len(nums) - 1, 0

        nums = sorted(nums)

        while i < j:
            add = nums[i] + nums[j]

            if add < k:
                i += 1
            elif add > k:
                j -= 1
            else:
                ret += 1
                i += 1
                j -= 1

        return ret