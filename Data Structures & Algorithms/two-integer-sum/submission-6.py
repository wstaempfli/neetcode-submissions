class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i in range(len(nums)):
            A.append([nums[i], i])
        
        A.sort()
        print(A)

        i, j = 0, len(nums) - 1

        while i != j:
            if A[i][0] + A[j][0] == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif A[i][0] + A[j][0] < target:
                i += 1
            elif A[i][0] + A[j][0] > target:
                j -= 1
        return []

