class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Idea: hashmap -> array -> sort -> first k elems 
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        l = list(d.items())
        l.sort(key=lambda x: x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res