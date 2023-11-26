class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []

        for num in range(n+1):
            ret.append(sum([int(i) for i in bin(num) if i == '1']))
        
        return ret