class Solution:
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j and j >= 0 and i < len(numbers):
            if (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]

            if numbers[j] > (target - numbers[i]):
                j -= 1
            elif numbers[i] < (target - numbers[j]):
                i += 1