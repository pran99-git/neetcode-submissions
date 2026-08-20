class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for indx in range(1, len(nums)):
            if nums[indx] == nums[indx-1]:
                return True
        return False