class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            d[key] = d.get(key, []) + [s]
        return list(d.values())