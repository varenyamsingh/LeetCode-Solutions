
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)

        n = len(squares)
        negative = n // 2

        return sum(squares[negative:]) - sum(squares[:negative])
