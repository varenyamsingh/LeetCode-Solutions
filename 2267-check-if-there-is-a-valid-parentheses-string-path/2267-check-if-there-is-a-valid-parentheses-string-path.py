from functools import lru_cache

class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')':
            return False

        @lru_cache(None)
        def dfs(r, c, balance):

            if balance < 0:
                return False

            remaining = (m - 1 - r) + (n - 1 - c)

            if balance > remaining:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            # Move down
            if r + 1 < m:
                next_balance = balance + (1 if grid[r + 1][c] == '(' else -1)

                if dfs(r + 1, c, next_balance):
                    return True

            # Move right
            if c + 1 < n:
                next_balance = balance + (1 if grid[r][c + 1] == '(' else -1)

                if dfs(r, c + 1, next_balance):
                    return True

            return False

        return dfs(0, 0, 1)