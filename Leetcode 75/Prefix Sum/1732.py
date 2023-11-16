class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        s = 0
        m = s

        for i,num in enumerate(gain):
            s = s + num
            if s > m:
                m = s

        return m