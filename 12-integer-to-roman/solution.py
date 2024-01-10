class Solution:
    def intToRoman(self, num: int) -> str:
        ans = 'M' * (num//1000)
        num %= 1000
        C = num//100
        if C == 4:
            ans += 'CD'
        elif C == 9:
            ans += 'CM'
        else:
            if C >= 5:
                ans += 'D'
            ans += 'C' * (C%5)
        num %= 100
        X = num//10
        if X == 4:
            ans += 'XL'
        elif X == 9:
            ans += 'XC'
        else:
            if X >= 5:
                ans += 'L'
            ans += 'X' * (X%5)
        num %= 10
        if num == 4:
            ans += 'IV'
        elif num == 9:
            ans += 'IX'
        else:
            if num >= 5:
                ans += 'V'
            ans += 'I' * (num%5)
        return ans