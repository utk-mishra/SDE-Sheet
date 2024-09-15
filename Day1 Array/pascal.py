#link: https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
         # my try -> top down too - didn't work - if leaf node has only one parent
    
        # complexity - O(n*n-1) - optimal

        # striver - formula based question - trivia - r-1 C n-1 

        # neetcode's add 0 to end and start, then two pointer

        res = [[1]]

        for i in range(numRows - 1):
            # add 0 at both ends of the parent row
            childArr = []
            parArr = [0] + res[-1] + [0]
            # traverse parent arr
            for j in range(len(res[-1]) + 1):
                childArr.append(parArr[j] + parArr[j+1])
            res.append(childArr)
        return res
    
        # time - O(n^2)
        # space - O(1) ??