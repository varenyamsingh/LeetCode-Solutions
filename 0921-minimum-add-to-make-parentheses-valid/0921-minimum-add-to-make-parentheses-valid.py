class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        answer = 0

        for ch in s:
            if ch == '(':
                balance += 1

            else:
                balance -= 1

                if balance < 0:
                    answer += 1
                    balance = 0

        answer += balance

        return answer