class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        
        max_suffix = [0] * n
        max_suffix[-1] = nums[-1]
        for k in range(n - 2, -1, -1):
            max_suffix[k] = max(max_suffix[k + 1], nums[k])
        
        max_i = nums[0]
        
        for j in range(1, n - 1):
            if max_i > nums[j]:  
                max_value = max(max_value, (max_i - nums[j]) * max_suffix[j + 1])
            max_i = max(max_i, nums[j])
        
        return max_value