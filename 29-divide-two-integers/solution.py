class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        s = abs(divisor)
        ans = 0
        bit = -1
        while s <= d:
            bit += 1
            s = s<<1
        s = s>>1
        while bit >= 0:
            if d >= s:
                d -= s
                ans = (ans<<1) + 1
            else:
                ans = ans<<1
            s = s>>1
            bit -= 1
        if (dividend >= 0 and divisor < 0) or (divisor >= 0 and dividend < 0):
            ans = -ans
        if ans > (2<<30)-1:
            return (2<<30)-1
        elif ans < -(2<<30):
            return -(2<<30)
        else:
            return ans