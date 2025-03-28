
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        contagem = Counter(nums)
        dominante, freq_dominante = contagem.most_common(1)[0]

        left_count = 0 
        right_count = freq_dominante 
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == dominante:
                left_count += 1
                right_count -= 1

            if left_count * 2 > (i + 1) and right_count * 2 > (n - i - 1):
                return i

        return -1