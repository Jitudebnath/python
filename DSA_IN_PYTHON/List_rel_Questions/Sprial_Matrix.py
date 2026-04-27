# print the element of the matrix in a particluar order in list means in spiral order


class Solution:
    def spiralOrder(self, matrix):
        result = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Left → Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Top → Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


# ---input Handling---

if __name__ == "__main__":
    rows, cols = map(int, input("Enter the rows and columns:").split())

    matrix = []
    print("Enter matix row by row")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    sol = Solution()
    result = sol.spiralOrder(matrix)
    print("Sprial Order", result)
