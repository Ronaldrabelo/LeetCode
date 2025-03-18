class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        mask = 0 
        max_length = 0 
        for right in range(n):
            while (mask & nums[right]) != 0:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            max_length = max(max_length, right - left + 1)

        return max_length