class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        n = len(expression)

        def concat(A, B):
            return {a + b for a in A for b in B}

        def parse_expression(i):
            # Handles union: A,B,C
            result = set()

            term, i = parse_term(i)
            result |= term

            while i < n and expression[i] == ',':
                i += 1

                term, i = parse_term(i)
                result |= term

            return result, i

        def parse_term(i):
            # Handles concatenation: ABC{d,e}
            result = {""}

            while i < n and expression[i] not in "},":
                factor, i = parse_factor(i)

                result = concat(result, factor)

            return result, i

        def parse_factor(i):
            # Letter
            if expression[i].islower():
                return {expression[i]}, i + 1

            # Braced expression
            i += 1  # skip {

            result, i = parse_expression(i)

            i += 1  # skip }

            return result, i

        result, _ = parse_expression(0)

        return sorted(result)