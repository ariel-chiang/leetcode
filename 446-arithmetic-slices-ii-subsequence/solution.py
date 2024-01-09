from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        # endDif[e][d]: number of subsequences with difference d looking for e
        endDif = defaultdict(lambda: defaultdict(int))
        for i in range(len(nums)):
            # add number of arithmetic slices ending with current number
            ans += sum(endDif[nums[i]].values())
            # look for new arithmetic slices with new ending numbers
            for d in endDif[nums[i]].keys():
                endDif[nums[i]+d][d] += endDif[nums[i]][d]
            # look for arithmetic slices generated by every two pair of numbers
            for j in range(i):
                endDif[nums[i]+nums[i]-nums[j]][nums[i]-nums[j]] += 1
        return ans