from collections import defaultdict
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort the jobs by end time
        jobs = sorted(zip(endTime, startTime, profit))

        # find the latest end time of each start time
        prev = defaultdict(int)
        endTime.sort()
        for s in startTime:
            if s not in prev and s >= endTime[0]:
                t = bisect.bisect_left(endTime, s)
                if endTime[t] > s:
                    prev[s] = endTime[t-1]
                else:
                    prev[s] = endTime[t]

        # record the max profit by each end time
        maxProfit = defaultdict(int)
        maxProfitTillNow = 0

        # the current max profit is either with or without the current job
        for e, s, p in jobs:
            maxProfit[e] = max(maxProfit[prev[s]]+p, maxProfitTillNow)
            maxProfitTillNow = max(maxProfitTillNow, maxProfit[e])

        return maxProfitTillNow