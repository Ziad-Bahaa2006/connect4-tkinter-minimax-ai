import copy
from sqlite3 import connect
import time
import math
import tkinter as tk
from tkinter import ttk, messagebox
import sys

rows = 6
cols = 7
empety = 0
player = 1
AI = 2
colors = {empety: "white", player: "red", AI: "blue"}

class connect4:

    def __init__(self, ROWS=rows, COLS=cols):  # كونستركتور
        self.rows = ROWS
        self.cols = COLS
        self.board = [[empety for _ in range(COLS)] for _ in range(ROWS)]
        self.last_move = None

    def copy(self):
        c = connect4(self.rows, self.cols)
        c.board = [row[:] for row in self.board]
        c.last_move = self.last_move
        return c

    def Valid_moves(self):
        return [c for c in range(self.cols) if self.board[0][c] == empety]

    def Make_move(self, col, piece):
        for r in reversed(range(self.rows)):
            if self.board[r][col] == empety:
                self.board[r][col] = piece     # ← كان هنا غلط (== بدل =)
                self.last_move = (r, col)      # ← كان كاتب cols غلط
                return True
        return False

    def Undo_move(self, col):
        for r in range(self.rows):
            if self.board[r][col] != empety:
                self.board[r][col] = empety    # ← كان فيه خطأ
                return True
        return False

    def is_full(self):
        return all(self.board[0][c] != empety for c in range(self.cols))

    def Check_winner(self, piece):
        # أفقي
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True

        # رأسي
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True

        # قطر موجب
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True

        # قطر سالب
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True

        return False

    def terminal_state(self):
        return self.Check_winner(player) or self.Check_winner(AI) or self.is_full()

    def print_board(self):
        for r in range(self.rows):
            print(self.board[r])
        print()

def evaluate_window(window, piece):
    score = 0
    opp_piece = player if piece == AI else AI

    count_piece = window.count(piece)
    count_opp = window.count(opp_piece)
    count_empty = window.count(empety)

    if count_piece == 4:
        score += 10000
    elif count_piece == 3 and count_empty == 1:
        score += 100
    elif count_piece == 2 and count_empty == 2:
        score += 10

    if count_opp == 3 and count_empty == 1:
        score -= 80

    return score

def heuristic(board: connect4, piece):
    score = 0
    rows = board.rows
    cols = board.cols
    b = board.board

    # center advantage
    center_col = cols // 2
    center_count = sum(1 for r in range(rows) if b[r][center_col] == piece)
    score += center_count * 6

    # horizontal
    for r in range(rows):
        for c in range(cols - 3):
            window = [b[r][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # vertical
    for c in range(cols):
        for r in range(rows - 3):
            window = [b[r+i][c] for i in range(4)]
            score += evaluate_window(window, piece)

    # positive diagonal
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [b[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # negative diagonal
    for r in range(3, rows):
        for c in range(cols - 3):
            window = [b[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score
