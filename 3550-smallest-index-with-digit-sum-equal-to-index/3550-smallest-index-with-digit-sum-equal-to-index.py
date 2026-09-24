class Solution:
    def smallestIndex(self, nums):
        ans = [
            i for i, num in enumerate(nums)
            if sum(map(int, str(num))) == i
        ]

        return ans[0] if ans else -1