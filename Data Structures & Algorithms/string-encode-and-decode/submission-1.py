class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            for c in s: 
                res.append(c)
                res.append(c)
            res.append('xy')
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        if(len(s) == 1):
            return [""]
        cur = []
        res = []
        i = 1
        while i < len(s):
            if s[i] != s[i-1]:
                res.append("".join(cur))
                cur = []
            else:
                cur.append(s[i])
            i += 2
        return res


