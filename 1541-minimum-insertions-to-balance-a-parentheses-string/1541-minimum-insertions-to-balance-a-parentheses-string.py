
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0

        for ch in s:
            if ch == '(':
                # An opening bracket needs two closing brackets
                need += 2

                # Keep required closing brackets in pairs
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

            else:
                need -= 1

                # Too many closing brackets
                if need < 0:
                    insertions += 1  # Insert '('
                    need = 1          # One more ')' is needed

        return insertions + need