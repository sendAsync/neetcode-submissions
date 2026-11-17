class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen= defaultdict(list)
        for _,s in enumerate(strs):
            key = tuple(sorted(s))
            seen[key].append(s)
        return list(seen.values())