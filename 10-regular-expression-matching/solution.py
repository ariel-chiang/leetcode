class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memoization for recursion
        mem = dict()
        def _isMatch(s: str, p: str) -> bool:
            if s+','+p in mem:
                return mem[s+','+p]
            if not p:
                return not s
            firstMatch = bool(s) and p[0] in {s[0], '.'}
            # if x* appears, either keep searching for x* or ignore the pattern
            if len(p) >= 2 and p[1] == '*':
                mem[s+','+p] = firstMatch and _isMatch(s[1:], p) \
                    or _isMatch(s, p[2:])
            else:
                mem[s+','+p] = firstMatch and _isMatch(s[1:], p[1:])
            return mem[s+','+p]
        return _isMatch(s, p)