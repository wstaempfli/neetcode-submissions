class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = []
        right_prods = []
        left_prods.append(1)
        right_prods.append(1)
        for i in range(1, len(nums)):
            left_prods.append(nums[i-1] * left_prods[i-1])
            right_prods.append(nums[len(nums) - i] * right_prods[i-1])
        right_prods.reverse()

        res = []
        for i in range(len(right_prods)):
            res.append(left_prods[i] * right_prods[i])
        return res