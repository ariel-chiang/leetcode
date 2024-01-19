class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minFall = matrix.copy()
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j > 0 and j < len(matrix[0])-1:
                    minFall[i][j] += min(minFall[i-1][j-1], minFall[i-1][j], minFall[i-1][j+1])
                elif j > 0:
                    minFall[i][j] += min(minFall[i-1][j-1], minFall[i-1][j])
                elif j < len(matrix[0])-1:
                    minFall[i][j] += min(minFall[i-1][j], minFall[i-1][j+1])
                else:
                    minFall[i][j] += minFall[i-1][j]
        return min(minFall[-1])