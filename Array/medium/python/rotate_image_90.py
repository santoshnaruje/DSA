from typing import List


class Solution:

    def transposeMatrix(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def roteteRow(self,matrix: List[List[int]]):
        for row in matrix:
            row.reverse()


    def rotate(self, matrix: List[List[int]]) -> None:
        self.transposeMatrix(matrix)
        self.roteteRow(matrix)
        print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    s = Solution()
    s.rotate(matrix)

