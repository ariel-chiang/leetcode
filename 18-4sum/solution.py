class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        ans = []

        # fix the first two numbers, then do two sum
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = j + 1
                h = len(nums)-1
                find = target-nums[i]-nums[j]
                while l < h:
                    s = nums[l]+nums[h]
                    if s == find:
                        ans.append(str(nums[i])+' '+str(nums[j])+' '+str(nums[l])+' '+str(nums[h]))
                        l += 1
                        h -= 1
                    elif s < find:
                        l += 1
                    else:
                        h -= 1
        return [map(int, s.split()) for s in list(set(ans))]