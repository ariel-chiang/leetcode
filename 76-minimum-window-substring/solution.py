from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        # sCount: count the # of chars (that exists in t) in the sliding window of s
        sCount = defaultdict(int)
        matches = len(t)
        right = -1
        # find the first valid window substring (with left=0)
        for i, c in enumerate(s):
            if c in tCount:
                sCount[c] += 1
                if sCount[c] <= tCount[c]:
                    matches -= 1
            if matches == 0:
                right = i
                break
        # if the entire string of s doesn't work, return empty string
        if right == -1:
            return ""
        # the first substring is a candidate answer
        ans = s[:right+1]
        # in each iteration, discard the first char (left+=1) and find valid substring
        for left in range(1, len(s)):
            c = s[left-1]
            if c in sCount:
                sCount[c] -= 1
                # right needs to be updated only if sCount[c] < tCount[c]
                # the goal is to find the next c (and keep sCount updated)
                if sCount[c] < tCount[c]:
                    currRight = right
                    for j in range(right+1, len(s)):
                        if s[j] in sCount:
                            sCount[s[j]] += 1
                        if s[j] == c:
                            right = j
                            break
                    # if right is not updated, then no more valid windows could be found
                    if right == currRight:
                        break
            # check if the new window has smaller length, update answer if so
            if right+1-left < len(ans):
                ans = s[left:right+1]
        return ans