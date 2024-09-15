class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # https://leetcode.com/problems/set-matrix-zeroes/
        # Q brief - Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.


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

        # optimal (space wise)
        # space complexity can be improved by using 0th row and col as reference for 0 presence
        # add only one var col0 for handling 0th col as [0,0] will be iused for 0th row
        col0 = 1
        # traverse the matrix to mark the 0th row and col
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # row array, orange
                    if j != 0: 
                         matrix[0][j] = 0 # col array, yellow
                    else:
                        col0 = 0

        # traverse the matrix barring 0 row and col, to mark element as 0 if either their row or col is 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Now handle the 0th row based on [0,0]
        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        # Now handle the 0th col based on col0
        if col0 == 0: 
            for i in range(len(matrix)):
                matrix[i][0] = 0

        # time complexity - O(2*n*m)
        # space complexity - O(1)