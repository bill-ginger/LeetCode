# hard

'''2020-03-21'''
import copy
class Solution:
    def NQueen(self, n, k, board, solution_list):
        if k == n:
            solution_list.append(copy.deepcopy(board))
            board = [-1] * n
            return
        for k_val in range(n):
            if k_val in board:
                continue
            flag = 0
            for j in range(k):
                if board[j] - k_val == j - k or board[j] - k_val == k - j:
                    flag = 1
                    break
            if flag:
                continue
            board[k] = k_val
            self.NQueen(n, k + 1, board, solution_list)
        board[k] = -1
        return
    def format_answer(self, n, solution_list):
        board_row = ['.'] * n
        answer_list = []
        for solution in solution_list:
            answer = []
            for col in range(n):
                board_row[solution[col]] = 'Q'
                ans_col = "".join(board_row)
                answer.append(ans_col)
                board_row = ['.'] * n
            answer_list.append(answer)
        return answer_list
    def solveNQueens(self, n):
        board = [-1] * n
        solution_list = []
        self.NQueen(n, 0, board, solution_list)
        return self.format_answer(n, solution_list)
