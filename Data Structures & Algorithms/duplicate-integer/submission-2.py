class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in nums:
            dup = 0
            for b in nums:
                if a == b:
                    dup += 1
            if dup >= 2:
                return True
        return False
        