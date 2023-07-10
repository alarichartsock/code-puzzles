class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(digit) for digit in digits)
        i = int(s)
        i += 1
        return [int(num) for num in list(str(i))]