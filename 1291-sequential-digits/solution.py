class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = '123456789'
        lowDigits = len(str(low))
        highDigits = len(str(high))
        ans = []
        for d in range(lowDigits, highDigits+1):
            for i in range(d, 10):
                num = int(seq[i-d:i])
                if num >= low and num <= high:
                    ans.append(num)
        return ans