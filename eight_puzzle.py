import math
import sys
import resource
import time
from search import bfs, dfs, ast

class EightPuzzle:
    def no_heuristic(self):
        return None

    def __init__(self, initial_board, heuristic=no_heuristic):
        self.initial_state = initial_board
        self.heuristic = heuristic

    def actions(self, board):
        possible_moves = []
        board = board.split(',')
        index = str(board.index('0'))
        if index not in ['0','1','2']:
            possible_moves.append('Up')
        if index not in ['6','7','8']:
            possible_moves.append('Down')
        if index not in ['0','3','6']:
            possible_moves.append('Left')
        if index not in ['2','5','8']:
            possible_moves.append('Right')
        return possible_moves

    def goal_test(self, board):
        return board == '0,1,2,3,4,5,6,7,8'

    def step_cost(self, _board, _action):
        return 1

    def result(self, board, action):
        board = board.split(',')
        zero_index = board.index('0')
        if action == 'Up':
            self.swap(board, zero_index-3)
        elif action == 'Down':
            self.swap(board, zero_index+3)
        elif action == 'Left':
            self.swap(board, zero_index-1)
        elif action == 'Right':
            self.swap(board, zero_index+1)
        else:
            return "ERROR"
        return ','.join(str(x) for x in board)

    def swap(self, board, new_index):
        zero_index = board.index('0')
        board[zero_index], board[new_index] = board[new_index], board[zero_index]
        return board

def manhattan_distance(board):
    total_distance = 0
    board = board.split(',')
    list_board = [int(n) for n in board]
    chunk_board = [list_board[n:n+3] for n in range(0, len(list_board), 3)]
    for index_row, board_row in enumerate(chunk_board):
        for index_column, number in enumerate(board_row):
            if number != 0:
                correct_row = math.floor(number / 3)
                correct_column = number % 3
                total_distance += abs(index_row - correct_row) + abs(index_column - correct_column)
    return total_distance

def main():
    search_type = sys.argv[1]
    board = sys.argv[2]
    if search_type == 'bfs':
        return bfs(EightPuzzle(board))
    elif search_type == 'dfs':
        return dfs(EightPuzzle(board))
    return ast(EightPuzzle(board, heuristic=manhattan_distance))

if __name__== "__main__":
    main()
