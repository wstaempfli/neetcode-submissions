class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}

        for s in strs:
            d = {}
            for c in s: 
                if c in d: 
                    d[c] += 1
                else: 
                    d[c] = 1
            k = frozenset(d.items())
            if k in master:
                master[k].append(s)
            else:
                master[k] = [s]
        res = []
        for v in master.values():
            res.append(v)
        return res

