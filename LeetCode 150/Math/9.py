class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = False
        
        x = str(x)
        
        if len(x) == 2:
            if x[0] == x[-1]:
                return True
        if len(x) == 1:
            return True
        
        start = x[0]
        end = x[-1]
        
        if start == end:
            return self.isPalindrome(x[1:-1])
        else:
            return False