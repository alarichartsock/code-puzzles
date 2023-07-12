class Solution:
    def isHappy(self, x):
        sqDigits = lambda x: sum(int(d) ** 2 for d in str(x))

        pastIts = set()

        while x not in pastIts:
            pastIts.add(x)

            x = sqDigits(x)

            if x == 1:
                return True

        return False