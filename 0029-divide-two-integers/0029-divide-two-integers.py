class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Handle sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            shift = 0

            # Find largest divisor * 2^shift
            while dividend >= (divisor << (shift + 1)):
                shift += 1

            # Add 2^shift to answer
            quotient += 1 << shift

            # Subtract divisor * 2^shift
            dividend -= divisor << shift

        # Apply sign
        if negative:
            quotient = -quotient

        # 32-bit integer limit
        if quotient > 2**31 - 1:
            return 2**31 - 1

        if quotient < -2**31:
            return -2**31

        return quotient