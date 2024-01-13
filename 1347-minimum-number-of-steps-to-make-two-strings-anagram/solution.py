from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        ans = 0
        for c in countT:
            if c in countS:
                ans += abs(countT[c]-countS[c])
            else:
                ans += countT[c]
        for c in countS:
            if c not in countT:
                ans += countS[c]
        return ans // 2