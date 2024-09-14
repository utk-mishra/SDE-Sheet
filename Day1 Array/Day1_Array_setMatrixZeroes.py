class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # https://leetcode.com/problems/set-matrix-zeroes/
        # if I find a zero, set everyhting in the row and column to zero - brute force - O(mn)
        # record all zeros, record the columns and rows in a set and then set them to zero - 
        # Keep record of all rows and columns set to 0, if already done don't. We must know the original zeroes.
        
        #Better soln achieved in 1st try! - optimal time complexity O(M*N)
        # rows = []
        # cols = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             if i not in rows:
        #                 rows.append(i)
        #             if j not in cols:
        #                 cols.append(j)
        # # print(rows, cols)
        # for r in rows:
        #     for i in range(len(matrix[0])):
        #         matrix[r][i] = 0
        # for c in cols:
        #     for j in range(len(matrix)):
        #         matrix[j][c] = 0
            
        #space complexity can be improved by using 0th row and col as reference for 0 presence
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # row array, orange
                    if j != 0: 
                         matrix[0][j] = 0 # col array, yellow
                    else:
                        col0 = 0

        print(matrix)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col0 == 0: 
            for i in range(len(matrix)):
                matrix[i][0] = 0