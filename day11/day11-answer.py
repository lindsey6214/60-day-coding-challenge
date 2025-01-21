class Solution: 
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
  
'''
Time complexity: O(m*n), where "m" is the number of rows in the matrix, and "n" is the number of columns. In the worst case, you need to visit every element in the matrix exactly once to collect them in a spiral order. Since there are m rows and n columns, there are m * n total elements in the matrix. The outer while loop runs as long as there are valid boundaries, which is at most min(m, n) / 2 times. In each iteration, you visit a constant number of elements (4) in the four directions.
Space complexity: O(1) because the algorithm does not use any data structures whose space requirements grow with the size of the matrix, it uses a constant amount of additional space.
'''
