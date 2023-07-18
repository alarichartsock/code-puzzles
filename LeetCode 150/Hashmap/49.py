class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sets = {}

        for s in strs:
            setstr = tuple(sorted(s))

            if setstr in sets.keys():
                sets[setstr].append(s)
            else:
                sets[setstr] = [s]
        
        ret = [sets[s] for s in sets.keys()]

        return ret
# I asked ChatGPT to rewrite my solution using only list comprehensions
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        [sets[tuple(sorted(s))].append(s) if tuple(sorted(s)) in sets.keys() else sets.update({tuple(sorted(s)): [s]}) for s in strs]
        return [sets[s] for s in sets.keys()]