class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {i: arr.count(i) for i in set(arr)}
        seen = list(d.values())

        if len(set(seen)) < len(seen):
            return False
        return True