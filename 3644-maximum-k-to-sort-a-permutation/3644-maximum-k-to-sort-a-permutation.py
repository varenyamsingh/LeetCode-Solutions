class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, num in enumerate(nums):
            if i != num:
                if k == -1:
                    k = num
                else:
                    k &= num

        return max(k, 0)
