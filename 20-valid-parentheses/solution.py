class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            elif stack:
                left = stack.pop()
                if ( c == ')' and left != '(' ) \
                    or ( c == '}' and left != '{' ) \
                    or ( c== ']' and left != '[' ):
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False