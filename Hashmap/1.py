# Brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if (i != j) and ( (num1 + num2) == target):
                    return [i,j]

# Hashmap solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i