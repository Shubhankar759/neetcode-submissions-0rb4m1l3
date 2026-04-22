class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            srotedS = ''.join(sorted(s))
            res[srotedS].append(s)

        return list(res.values())
