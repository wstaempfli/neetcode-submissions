class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a, b, c, d, e, f] -> [bcdef, acdef, abdef, abcef, abcdf, abcde]
        prod = 1
        zero = -1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if zero >= 0:
                    return [0] * len(nums)
                else:
                    zero = i
            else: 
                prod *= num
        
        res = []
        if zero >= 0:
            res = [0] * len(nums)
            res[zero] = prod
        else:
            for num in nums:
                res.append(prod//num)
        return res