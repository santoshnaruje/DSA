# Set Matrix Zeroes (LeetCode 73)
# Created by santosh

class Solution:
    def set_matrix_zero_brute_force(self, matrix: list[list[int]]) -> None:
        """
        Brute force: find zeros first, then mark rows and columns.
        Time: O(m*n*(m+n)), Space: O(k) for zero positions
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for row, col in zeros:
            for k in range(n):
                matrix[row][k] = 0
            for k in range(m):
                matrix[k][col] = 0


if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    s = Solution()
    s.set_matrix_zero_brute_force(matrix)
    for row in matrix:
        print(" ".join(map(str, row)))
