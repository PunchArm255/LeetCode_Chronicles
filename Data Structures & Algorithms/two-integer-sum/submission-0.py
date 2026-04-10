class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        res = []
        for i in range(len(nums)):
            j = 0
            for j in range(len(nums)):
                if i != j and (nums[i] + nums[j] == target):
                    res = [i, j]
                    return res
                j += 1
            i += 1
