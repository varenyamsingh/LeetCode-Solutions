
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)

        # Buy combined items for common requirements
        cost = common * min(costBoth, cost1 + cost2)

        # Buy remaining individual items
        cost += (need1 - common) * min(cost1, costBoth)
        cost += (need2 - common) * min(cost2, costBoth)

        return cost
