class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        count = 1
        for indx in range(1, len(nums)):
            diff = nums[indx] - nums[indx-1]
            if diff == 1:
                count += 1
            elif diff > 1:
                count = 1
            max_len = max(max_len, count)
        return max_len