"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def 
    (self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False

    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " "  # indicate used cell
            # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and self.exist_helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and self.exist_helper(board, word[1:], i, j + 1):
                return True
            board[i][j] = word[0]  # update the cell to its original value
            return False
        else:
            return False