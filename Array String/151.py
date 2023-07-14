# One liner
# Beats 99.4% runtime, beats 99.43% memory
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]).strip()