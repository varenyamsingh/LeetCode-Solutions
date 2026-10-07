class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, current, balance, left, right):

            # Too many closing parentheses
            if balance < 0:
                return

            # End of string
            if index == len(s):

                if balance == 0 and left == 0 and right == 0:
                    result.add(''.join(current))

                return

            ch = s[index]

            # Remove current '('
            if ch == '(' and left > 0:
                dfs(
                    index + 1,
                    current,
                    balance,
                    left - 1,
                    right
                )

            # Remove current ')'
            if ch == ')' and right > 0:
                dfs(
                    index + 1,
                    current,
                    balance,
                    left,
                    right - 1
                )

            # Keep current character
            current.append(ch)

            if ch == '(':
                dfs(
                    index + 1,
                    current,
                    balance + 1,
                    left,
                    right
                )

            elif ch == ')':
                dfs(
                    index + 1,
                    current,
                    balance - 1,
                    left,
                    right
                )

            else:
                dfs(
                    index + 1,
                    current,
                    balance,
                    left,
                    right
                )

            current.pop()

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)