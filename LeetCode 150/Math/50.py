# Implements the babylonian squaring algorithm.
class Solution:
    def mySqrt(self, n):
        x = n
        y = 1
        # e decides the accuracy level
        e = 0.000001
        while(x - y > e):
            x = (x + y)/2
            y = n / x
        return round(x // 1)
