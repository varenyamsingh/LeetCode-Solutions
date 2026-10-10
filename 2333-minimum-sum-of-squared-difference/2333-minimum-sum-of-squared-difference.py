
from typing import List

class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int],
        k1: int, k2: int
    ) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        low, high = 0, max(diffs)

        while low < high:
            mid = (low + high) // 2

            needed = sum(max(d - mid, 0) for d in diffs)

            if needed <= k:
                high = mid
            else:
                low = mid + 1

        level = low
        needed = sum(max(d - level, 0) for d in diffs)
        remaining = k - needed

        diffs = [min(d, level) for d in diffs]

        for i in range(len(diffs)):
            if remaining == 0:
                break

            if diffs[i] == level:
                diffs[i] -= 1
                remaining -= 1

        return sum(d * d for d in diffs)