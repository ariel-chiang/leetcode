class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for r in range(numRows)]
        j = 0
        add = True
        for i in range(len(s)):
            rows[j].append(s[i])
            # handle zigzag
            if add and j < numRows-1:
                j += 1
            elif not add and j > 0:
                j -= 1
            elif add:
                add = False
                j -= 1
            else:
                add = True
                j += 1
        return ''.join([''.join(rows[r]) for r in range(numRows)])