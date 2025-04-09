from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1
        
        maiores_que_k = {num for num in nums if num > k}
        
        return len(maiores_que_k)
