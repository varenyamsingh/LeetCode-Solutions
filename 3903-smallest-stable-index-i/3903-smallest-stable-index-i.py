class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
            n = len(nums)

            for i in range(n):
                prefix_max = max(nums[:i + 1])
                suffix_min = min(nums[i:])

                if prefix_max - suffix_min <= k:
                    return i

            return -1