from typing import List


class Solution:
    def setZeroesBruteForce(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:

                    # Mark all the columns to -1
                    for row in range(rows):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -1

                    # Mark all the rows to -1

                    for col in range(cols):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -1
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

    def setZeroBetterSolution(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        all_zero_rows = set();
        all_zero_cols = set();
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    all_zero_rows.add(i)
                    all_zero_cols.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in all_zero_rows or j in all_zero_cols:
                    matrix[i][j] = 0

    def setMatrixZeroOptimalSolution(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        firstRowZero = any(matrix[0][j]==0 for j in range(cols))
        firstColZero = any(matrix[i][0]==0 for i in range(rows))

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    # Mark first row as zero
                    matrix[i][0] = 0

                    # Mark first col as Zero
                    matrix[0][j] = 0

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0


if __name__ == "__main__":
    nums = [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]

    Solution().setMatrixZeroOptimalSolution(nums)
    for row in nums:
        for el in row:
            print(el,end=" ")
        print()
