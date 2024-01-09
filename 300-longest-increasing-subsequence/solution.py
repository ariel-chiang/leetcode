import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # endOfSub[i] is the smallest ending number of a strictly increasing subsequence of length i
        endOfSub = [10001]

        for num in nums:
            idx = bisect.bisect_left(endOfSub, num)
            if idx >= len(endOfSub):
                endOfSub.append(num)
            elif endOfSub[idx] != num:
                endOfSub[idx] = num
                
        return len(endOfSub)