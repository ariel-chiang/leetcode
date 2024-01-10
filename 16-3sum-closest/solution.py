class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        # fix the smallest number, then do 2-sum
        for i in range(len(nums)):
            l = i+1
            h = len(nums)-1
            while l < h:
                curr = nums[i] + nums[l] + nums[h]
                if abs(curr-target) < abs(ans-target):
                    ans = curr
                if curr > target:
                    h -= 1
                elif curr < target:
                    l += 1
                else:
                    return target
        return ans