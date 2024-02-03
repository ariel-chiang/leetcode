class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # maxSum[j]: largest sum of arr[0]+...+arr[j-1]
        maxSum = [0]
        for i in range(len(arr)):
            tempSum = 0
            for j in range(max(0, i-k+1), i+1):
                tempSum = max(maxSum[j]+max(arr[j:i+1])*(i+1-j), tempSum)
            maxSum.append(tempSum)
        print(maxSum)
        return maxSum[-1]