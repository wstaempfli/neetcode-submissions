class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1,d2 = {}, {}

        for a,b in zip(s,t):
            d1[a] = 1 + d1.get(a, 0)
            d2[b] = 1 + d2.get(b, 0)
        if d1 != d2:
            return False
        return True

        